"""Approximate Bayesian computation for the behavioural parameters, 2005–2023.

For each election the party votes in every electorate are taken as given
(they are observed). Only how voters split their two ticks is simulated, with
the same mechanisms the calibrated Monte Carlo uses:

  π        personal vote: share of every party's voters who vote for a
           candidate they like, spread over the candidates standing in
           proportion to sqrt(local party vote) × appeal, where each
           candidate's appeal is lognormal with spread σ_a.
  s_q      strategic voting, one rate per partner party q (every party other
           than Labour, National, the Māori parties and the centrists): share
           of its remaining voters who back their bloc leader's candidate.
  s_L, s_R the same for centrists and pooled tiny parties allied to each bloc
           (simulated, but not fitted: see below).
  s_M      in Māori electorates, the share of Labour's voters backing the
           locally strongest Māori-party candidate;
  s_Mo     the same for other Left voters (Greens, allied centrists, ...).
  n_st, d  standout candidates: n_st smaller-party candidates, each placed in
           one of its side's stronger electorates (weight ∝ local share³ ×
           side's local share⁶), where a share d of the voters who would have
           backed their bloc leader back the standout instead.

Priors: π ~ U(0, 0.30), each s_q, s_L, s_R ~ U(0, 1), s_M, s_Mo ~ U(0, 0.8), σ_a ~ U(0, 2),
n_st ~ U{0..8}, d ~ U(0.2, 1).

Summary statistics, compared with what actually happened:
  • national split-vote rows, general electorates: for each party with 1%+,
    the share of its voters whose electorate vote went to its own candidate,
    Labour's, and National's;
  • Māori electorates: the share of Labour, Green and Māori-party voters
    backing a Māori-party candidate;
  • electorate-by-electorate error in Labour's and National's candidate vote
    shares (general electorates) and Māori parties' (Māori electorates);
  • number of general electorates won by a party other than Labour or
    National, and the three highest such candidates' vote shares;
  • number of Māori electorates won by a Māori party.
Each statistic is scaled by its spread across the prior draws; the electorate-
win statistics, which carry most of the evidence on standouts, are weighted
up (non-leader wins and top shares ×4, Māori-party wins ×2). The 2% of draws
closest to the actual election are kept, weighted by an Epanechnikov kernel on
that distance, and then regression-adjusted (Beaumont, Zhang & Balding 2002):
each parameter is regressed on the statistics' gaps from the observed values,
and the fitted gap effect is removed. Only well-identified parameters are
adjusted: π, s_M, s_Mo, and the strategic rates of partner parties with at least 2%
of the party vote. The rest (σ_a, n_st, d, and rates for tiny parties) keep
their kernel-weighted rejection draws, because a linear adjustment pushes
weakly identified parameters onto the prior's bounds. Draws are resampled by
weight to 1,000.

Posterior-predictive check: 300 posterior draws are re-simulated and their
mean summary statistics compared with the actual election (abc_summary.md).

Prior draws and statistics are cached in abc_cache/<year>.npz, so the
posterior can be recomputed without re-simulating.

Centrist parties (NZ First, United Future, TOP) are simulated but left out of
the fit: their voters' electorate votes split between both leaders, which the
model's "one ally" rule doesn't represent. (TOP's candidate votes are also
filed under "TOP" in the saved data, so its split-vote row is unusable.)

A party's voters with no candidate of their own in an electorate back the
strategic target at the usual rate; the rest spread over the candidates like
personal votes.

Simplifications: a party "stands" in an electorate if its candidate got at
least 1%; votes for parties under 0.5% are pooled and follow the actual
national pattern of where those voters' electorate votes went.

Run:  python3 abc_history.py [draws per election]   (default 20000)
      → abc_posterior.json, abc_summary.md
"""
import json
import math
import random
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np

import mc_history as h

ROOT = Path(__file__).parent
LAB, NAT = "LABOUR PARTY", "NATIONAL PARTY"
PARAMS = ["pi", "s_M", "s_Mo", "sigma_a", "n_st", "d"]
KEEP = 0.02
STAT_WEIGHT = {"nonleader_wins": 4.0, "top_nonleader": 4.0, "maori_party_wins": 2.0}
BOUNDS = {"pi": (0, 0.30), "s_M": (0, 0.8), "s_Mo": (0, 0.8), "sigma_a": (0, 2), "n_st": (0, 8), "d": (0.2, 1.0)}


def prior(rng, partners):
    th = {"pi": rng.uniform(0, 0.30), "s_L": rng.random(), "s_R": rng.random(),
          "s_M": rng.uniform(0, 0.8), "s_Mo": rng.uniform(0, 0.8), "sigma_a": rng.uniform(0, 2),
          "n_st": rng.randint(0, 8), "d": rng.uniform(0.2, 1.0)}
    th["s_party"] = {p: rng.random() for p in partners}
    return th


# ---------------------------------------------------------------- data

class Election:
    def __init__(self, year):
        d = h.load(year)
        self.year = year
        pl = d["plist"]
        self.pl = pl
        K = len(pl)
        self.K = K
        self.ally = np.array([h.bloc_of(d, year, p)[0] for p in pl])
        self.lab, self.nat = pl.index(LAB), pl.index(NAT)
        self.maori = np.array([p in h.MAORI_PARTIES for p in pl])
        self.leader = {"L": self.lab, "R": self.nat}
        from calibrate_history import CENTRE
        self.partners = [p for i, p in enumerate(pl)
                         if i not in (self.lab, self.nat) and not self.maori[i] and p not in CENTRE]
        self.votes = {p: d["votes"][p] for p in pl}
        els = [e for e in d["el"] if len(e) == 6]          # drop cancelled polls
        self.is_m = np.array([e[1] == 1 for e in els])
        tv = np.array([e[3] for e in els], float)
        ps = np.array([e[4] for e in els], float) / 1000
        self.cs_obs = np.array([e[5] for e in els], float) / 1000
        self.pv = ps * tv[:, None]                        # party votes by electorate
        self.other = tv - self.pv.sum(1)                   # pooled tiny parties
        self.stand = self.cs_obs >= 0.01
        self.win_obs = np.array([e[2] if isinstance(e[2], int) else -1 for e in els])
        # where the pooled tiny parties' voters' electorate votes went, nationally
        ox = d["xt"]["gen"].get("#OTHER", {})
        self.other_dest = np.array([ox.get(p, 0) for p in pl], float)
        # observed national split-vote rows (general and Māori electorates)
        self.obs_stats = self.observed_stats(d)

    def observed_stats(self, d):
        S = {}
        g = d["xt"]["gen"]
        tot = d["total"]
        from calibrate_history import CENTRE
        for i, p in enumerate(self.pl):
            if d["votes"][p] / tot < 0.01 or self.maori[i] or p in CENTRE:
                continue
            r = g.get(p, {})
            n = sum(r.get(c, 0) for c in self.pl)
            if not n:
                continue
            S[f"gen:{p}:own"] = r.get(p, 0) / n
            if i != self.lab:
                S[f"gen:{p}:lab"] = r.get(LAB, 0) / n
            if i != self.nat:
                S[f"gen:{p}:nat"] = r.get(NAT, 0) / n
        mx = d["xt"]["mao"]
        mps = [p for i, p in enumerate(self.pl) if self.maori[i]]
        for p in [LAB, "GREEN PARTY"] + mps:
            r = mx.get(p, {})
            n = sum(r.get(c, 0) for c in self.pl)
            if n and p in self.pl:
                S[f"mao:{p}:tomaori"] = sum(r.get(c, 0) for c in mps) / n
        gen = ~self.is_m
        nl = [w for w, m in zip(self.win_obs, self.is_m) if not m and w not in (self.lab, self.nat)]
        S["nonleader_wins"] = len(nl)
        top = sorted((self.cs_obs[e, c] for e in np.where(gen)[0] for c in range(self.K)
                      if c not in (self.lab, self.nat)), reverse=True)[:3]
        for k, x in enumerate(top):
            S[f"top_nonleader_{k}"] = x
        S["maori_party_wins"] = int(sum(1 for w, m in zip(self.win_obs, self.is_m)
                                        if m and w >= 0 and self.maori[w]))
        return S

    # ------------------------------------------------------------ simulate

    def simulate(self, th, rng):
        K = self.K
        E = len(self.pv)
        nprng = np.random.default_rng(rng.getrandbits(32))
        Ms = np.zeros((E, K, K))
        for e in range(E):
            pv, st = self.pv[e], self.stand[e]
            cands = np.where(st)[0]
            if not len(cands):
                continue
            app = np.zeros(K)
            app[cands] = np.sqrt(np.maximum(pv[cands], 1)) * np.exp(nprng.normal(0, th["sigma_a"], len(cands)))
            app /= app.sum()
            M = np.outer(pv * th["pi"], app)
            rest = pv * (1 - th["pi"])
            mt = None
            if self.is_m[e]:
                mc = [c for c in cands if self.maori[c]]
                if mc:
                    mt = max(mc, key=lambda c: pv[c])
            for q in range(K):
                if rest[q] <= 0:
                    continue
                a = self.ally[q]
                if mt is not None and a == "L":
                    tgt, s = mt, th["s_M"] if q == self.lab else th["s_Mo"]
                else:
                    tgt = self.leader[a]
                    s = th["s_party"].get(self.pl[q], th["s_L" if a == "L" else "s_R"])
                if not st[tgt]:
                    tgt = q if st[q] else None
                if tgt is None:
                    M[q] += rest[q] * app
                    continue
                if tgt == q:
                    s = 0.0
                M[q, tgt] += rest[q] * s
                if st[q]:
                    M[q, q] += rest[q] * (1 - s)
                else:   # no candidate of their own: the non-strategic rest spread like personal votes
                    M[q] += rest[q] * (1 - s) * app
            Ms[e] = M
        # standouts
        gen = np.where(~self.is_m)[0]
        elig = [c for c in range(K) if c not in (self.lab, self.nat) and not self.maori[c]]
        used = set()
        for _ in range(th["n_st"] if elig else 0):
            c = rng.choice(elig)
            a = self.ally[c]
            side = self.ally == a
            opts = [e for e in gen if e not in used and self.stand[e, c]]
            if not opts:
                continue
            tv = self.pv[opts].sum(1) + self.other[opts]
            w = (self.pv[opts, c] / tv) ** 3 * (self.pv[opts][:, side].sum(1) / tv) ** 6
            if w.sum() <= 0:
                continue
            e = rng.choices(opts, weights=w.tolist())[0]
            used.add(e)
            ldr = self.leader[a]
            for q in np.where(side)[0]:
                if q != c:
                    mv = th["d"] * Ms[e, q, ldr]
                    Ms[e, q, ldr] -= mv; Ms[e, q, c] += mv
        cand = Ms.sum(1)
        # pooled tiny parties
        for e in range(E):
            dest = self.other_dest * self.stand[e]
            if dest.sum() > 0:
                cand[e] += self.other[e] * dest / dest.sum()
        return Ms, cand

    def stats(self, Ms, cand):
        S = {}
        gen = ~self.is_m
        G = Ms[gen].sum(0)
        for key in self.obs_stats:
            parts = key.split(":")
            if parts[0] == "gen":
                i = self.pl.index(parts[1])
                n = G[i].sum()
                j = {"own": i, "lab": self.lab, "nat": self.nat}[parts[2]]
                S[key] = G[i, j] / n if n else 0.0
            elif parts[0] == "mao":
                Mm = Ms[self.is_m].sum(0)
                i = self.pl.index(parts[1])
                n = Mm[i].sum()
                S[key] = Mm[i, self.maori].sum() / n if n else 0.0
        share = cand / np.maximum(cand.sum(1, keepdims=True), 1)
        # cand_obs shares are of all candidate votes; rescale ours to the same total
        share = share * self.cs_obs.sum(1, keepdims=True)
        win = np.where(self.stand.any(1), cand.argmax(1), -1)
        nl = [w for w, m in zip(win, self.is_m) if not m and w not in (self.lab, self.nat)]
        S["nonleader_wins"] = len(nl)
        top = sorted((share[e, c] for e in np.where(gen)[0] for c in range(self.K)
                      if c not in (self.lab, self.nat)), reverse=True)[:3]
        for k in range(3):
            if f"top_nonleader_{k}" in self.obs_stats:
                S[f"top_nonleader_{k}"] = top[k] if k < len(top) else 0.0
        S["maori_party_wins"] = int(sum(1 for w, m in zip(win, self.is_m) if m and w >= 0 and self.maori[w]))
        # electorate-by-electorate errors (target 0)
        S["rmse_leaders"] = float(np.sqrt(np.mean((share[gen][:, [self.lab, self.nat]]
                                                    - self.cs_obs[gen][:, [self.lab, self.nat]]) ** 2)))
        if self.maori.any() and self.is_m.any():
            S["rmse_maori"] = float(np.sqrt(np.mean((share[self.is_m][:, self.maori].sum(1)
                                                     - self.cs_obs[self.is_m][:, self.maori].sum(1)) ** 2)))
        return S


_EL = {}


def one(args):
    year, k = args
    if year not in _EL:
        _EL[year] = Election(year)
    el = _EL[year]
    rng = random.Random(year * 1_000_003 + k)
    th = prior(rng, el.partners)
    S = el.stats(*el.simulate(th, rng))
    return th, S


def flat_theta(th, partners):
    return [th[p] for p in BOUNDS] + [th["s_party"][q] for q in partners]


def abc(year, n, pool):
    el = Election(year)
    cache = ROOT / "abc_cache" / f"{year}.npz"
    obs = dict(el.obs_stats)
    obs["rmse_leaders"] = 0.0
    if el.maori.any():
        obs["rmse_maori"] = 0.0
    keys = list(obs)
    if cache.exists() and int(np.load(cache)["n"]) >= n:
        z = np.load(cache)
        X, T = z["X"][:n], z["T"][:n]
    else:
        res = pool.map(one, [(year, k) for k in range(n)], chunksize=50)
        X = np.array([[S[k] for k in keys] for _, S in res], float)
        T = np.array([flat_theta(th, el.partners) for th, _ in res], float)
        cache.parent.mkdir(exist_ok=True)
        np.savez_compressed(cache, X=X, T=T, n=n)
    return regress_adjust(el, keys, obs, X, T, n)


def regress_adjust(el, keys, obs, X, T, n):
    o = np.array([obs[k] for k in keys])
    sd = X.std(0)
    sd[sd == 0] = 1
    Z = (X - o) / sd
    # the few statistics on electorate wins carry the standout evidence; weight them up
    wt = np.array([STAT_WEIGHT.get(k.split(":")[0] if ":" in k else k.rstrip("012").rstrip("_"), 1.0) for k in keys])
    dist = np.sqrt(np.average(Z ** 2, axis=1, weights=wt))
    acc = np.argsort(dist)[: int(KEEP * n)]
    hmax = dist[acc].max()
    w = 1 - (dist[acc] / hmax) ** 2
    A = np.hstack([np.ones((len(acc), 1)), Z[acc]])
    WA = A * w[:, None]
    beta = np.linalg.lstsq(WA.T @ A + 1e-6 * np.eye(A.shape[1]), WA.T @ T[acc], rcond=None)[0]
    names = list(BOUNDS) + el.partners
    tot = sum(el.votes.values())
    adjust = np.array([nm in ("pi", "s_M", "s_Mo") or (nm in el.partners and el.votes[nm] / tot >= 0.02)
                       for nm in names])
    adj = T[acc] - (Z[acc] @ beta[1:]) * adjust
    lo = np.array([BOUNDS[p][0] for p in BOUNDS] + [0.0] * len(el.partners))
    hi = np.array([BOUNDS[p][1] for p in BOUNDS] + [1.0] * len(el.partners))
    adj = np.clip(adj, lo, hi)
    rng = np.random.default_rng(el.year)
    pick = rng.choice(len(acc), size=1000, p=w / w.sum())
    post = []
    for i in pick:
        th = {nm: float(adj[i, j]) for j, nm in enumerate(names[:len(BOUNDS)])}
        th["n_st"] = int(round(th["n_st"]))
        th["s_party"] = {q: float(adj[i, len(BOUNDS) + j]) for j, q in enumerate(el.partners)}
        post.append(th)
    # posterior-predictive check
    prng = random.Random(el.year)
    sims = []
    for th in post[:300]:
        th = dict(th, s_L=prng.random(), s_R=prng.random())
        S = el.stats(*el.simulate(th, prng))
        sims.append([S[k] for k in keys])
    sims = np.array(sims, float)
    fit = {k: {"observed": round(float(obs[k]), 3),
               "accepted_mean": round(float(sims[:, j].mean()), 3),
               "prior_mean": round(float(X[:, j].mean()), 3)} for j, k in enumerate(keys)}
    return post, fit, float(np.median(dist[acc])), el


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    out, lines = {}, []
    with Pool() as pool:
        for y in h.YEARS:
            post, fit, dist, el = abc(y, n, pool)
            for t in post:   # vote-weighted bloc averages of the partner rates
                for b in "LR":
                    ps = [p for p in el.partners if el.ally[el.pl.index(p)] == b]
                    w = sum(el.votes[p] for p in ps)
                    t[f"s_{b}_partners"] = (sum(t["s_party"][p] * el.votes[p] for p in ps) / w) if w else None
            out[y] = {"posterior": post, "fit": fit, "accepted_distance_median": round(dist, 3),
                      "partners": {p: el.ally[el.pl.index(p)] for p in el.partners}}
            show = {p: f"{np.median([t[p] for t in post]):.2f} [{q([t[p] for t in post], .05):.2f}, "
                       f"{q([t[p] for t in post], .95):.2f}]" for p in PARAMS}
            show.update({p.title()[:18]: f"{np.median([t['s_party'][p] for t in post]):.2f} "
                         f"[{q([t['s_party'][p] for t in post], .05):.2f}, {q([t['s_party'][p] for t in post], .95):.2f}]"
                         for p in el.partners})
            print(y, show, flush=True)
    (ROOT / "abc_posterior.json").write_text(json.dumps(out, indent=1))

    lines.append(f"# ABC posteriors for behavioural parameters ({n} prior draws per election, top {KEEP:.1%} kept)\n")
    lines.append("Median [5th–95th percentile] of accepted draws.\n")
    lines.append("| Year | " + " | ".join(PARAMS) + " |")
    lines.append("|---|" + "---|" * len(PARAMS))
    for y, v in out.items():
        po = v["posterior"]
        lines.append(f"| {y} | " + " | ".join(
            f"{np.median([t[p] for t in po]):.2f} [{q([t[p] for t in po], .05):.2f}–{q([t[p] for t in po], .95):.2f}]"
            for p in PARAMS) + " |")
    allp = [t for v in out.values() for t in v["posterior"]]
    lines.append("| **pooled** | " + " | ".join(
        f"{np.median([t[p] for t in allp]):.2f} [{q([t[p] for t in allp], .05):.2f}–{q([t[p] for t in allp], .95):.2f}]"
        for p in PARAMS) + " |")
    lines.append("\n## Strategic rate for each partner party (s_q)\n")
    lines.append("| Year | Party | Bloc | Median [5th–95th] |\n|---|---|---|---|")
    for y, v in out.items():
        for p, b in v["partners"].items():
            xs = [t["s_party"][p] for t in v["posterior"]]
            lines.append(f"| {y} | {p.title()} | {b} | {np.median(xs):.2f} [{q(xs, .05):.2f}–{q(xs, .95):.2f}] |")
    lines.append("\n## Fit: observed vs posterior-mean summary statistics\n")
    for y, v in out.items():
        lines.append(f"\n### {y}\n\n| Statistic | Observed | Posterior predictive mean | Prior mean |\n|---|---|---|---|")
        for k, f in v["fit"].items():
            lines.append(f"| {k} | {f['observed']} | {f['accepted_mean']} | {f['prior_mean']} |")
    (ROOT / "abc_summary.md").write_text("\n".join(lines) + "\n")
    print("wrote abc_posterior.json, abc_summary.md")


if __name__ == "__main__":
    main()
