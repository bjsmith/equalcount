"""Build the GitHub Pages site in docs/.

Nothing in the project is moved: every page is generated from the working
files where they live, so other work can carry on editing them.

  site/counted-twice.html        -> docs/index.html          (2023 explainer, the landing page)
  site/counted-twice-2026.html   -> docs/2026/index.html     (2026 explainer)
  overall_report.md + appendices -> docs/report/*.html       (full analysis, rendered from markdown)
  DATASETS / scripts below       -> docs/data/index.html     (data & code index, sizes read at build time)

Run:  pip install -r requirements.txt   (once; needs the `markdown` package)
      python3 build_site.py

Set REPO_URL (or the OVERHANG_REPO_URL environment variable) to the GitHub
repository so file names on the report and data pages link to the source.
"""
import ast
import datetime as dt
import html
import os
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
REPO_URL = os.environ.get("OVERHANG_REPO_URL", "https://github.com/bjsmith/equalcount").rstrip("/") or None
BRANCH = "main"
TODAY = dt.date.today()

# ---------------------------------------------------------------- explainers
PAGES = [
    ("counted-twice.html", "index.html",
     "How about 41,000 split ballots affected Parliament in 2023, and a proposed change to the overhang rules.",
     "One Ballot, Counted Twice",
     "How split voting gave Parliament 2 overhang seats in 2023, and how a proposed rule change would keep seats in line with the party vote."),
    ("counted-twice-2026.html", "2026/index.html",
     "How split voting gave the 2026 Parliament 11 overhang seats, and how a proposed change to the overhang rules would work. Based on the preliminary count.",
     "One Ballot, Counted Twice (2026)",
     "National and Te Pāti Māori won 11 overhang seats in 2026. See how a proposed rule change would keep Parliament at 120 seats."),
]

# ------------------------------------------------------------------- reports
# (source markdown, output path under docs/, short title for navigation)
REPORTS = [
    ("overall_report.md", "report/index.html", "Full report"),
    ("overhang-transfer-explainer.md", "report/transfer-explainer.html", "The proposal, explained"),
    ("experiment1_report.md", "report/experiment-1.html", "Experiment 1: stress test"),
    ("report_experiment2.md", "report/experiment-2.html", "Experiment 2: NZ elections 2005–2023"),
    ("report_experiment3.md", "report/experiment-3.html", "Experiment 3: futures from 2026"),
]

# ---------------------------------------------------------------------- data
# Files that are too large or too frequently regenerated for git history.
# They are gitignored and published as a GitHub Release asset by
# make_data_release.sh.
RELEASE_ONLY = [
    "runs/*/records.jsonl.gz", "runs/*/measures.csv",
    "paradox_results.csv", "paradox_recheck.csv",
]

DATASETS = [
    ("Inputs", [
        ("data/raw/2023/", "Electoral Commission 2023 results and split-vote tables (general and Māori electorates)."),
        ("data/raw/2026_preliminary/", "2026 preliminary count by electorate and nationally (special votes not included)."),
        ("data/raw/history/", "Election results 2005–2023 used for the historical recounts and calibration."),
        ("2026_Preliminary_Results_-_Vote_Splitting_Analysis.xlsx", "Spreadsheet working of the 2026 preliminary vote-splitting estimate."),
    ]),
    ("Worked examples", [
        ("results_2023.json", "2023 under the transfer rule (the explainer's example)."),
        ("results_2026.json", "2026 provisional result and transfer estimate."),
        ("results_levelling.json", "Extra list seats needed for full proportionality, with and without the transfer."),
        ("results_straight_ticket.json", "Counterfactual where every voter votes a straight ticket."),
    ]),
    ("Experiment 1: synthetic stress test", [
        ("mc_results.csv", "One row per scenario (5,000), every rule applied to the same ballots."),
        ("mc_summary.md", "Summary tables."),
        ("runs/exp1/records.jsonl.gz", "Raw ballot states for every scenario."),
        ("runs/exp1/measures.csv", "Shared measures computed from the raw states."),
    ]),
    ("Experiment 2: New Zealand elections and calibrated scenarios", [
        ("results_history.json", "2005–2023 recounted under each rule."),
        ("calibration.json", "Parameters measured from 2005–2023."),
        ("abc_posterior.json", "Approximate Bayesian computation posterior for the behavioural parameters."),
        ("mc_results_calibrated.csv", "One row per calibrated scenario (5,000)."),
        ("mc_summary_calibrated.md", "Summary tables."),
        ("runs/exp2_history/records.jsonl.gz", "Raw ballot states, actual elections."),
        ("runs/exp2/records.jsonl.gz", "Raw ballot states, calibrated scenarios."),
        ("runs/exp2/measures.csv", "Shared measures computed from the raw states."),
    ]),
    ("Experiment 3: adaptive futures from 2026", [
        ("futures/", "Stage 1: ten futures reasoned election by election (digests, reasoning, overrides)."),
        ("runs/exp3_baseline/results.csv", "Stage 2: 1,000 walks × 5 elections × each rule."),
        ("runs/exp3_copycat/results.csv", "Scenario where other blocs copy the split-list strategy."),
        ("runs/exp3_escalation/results.csv", "Scenario where split-list strategies escalate."),
        ("runs/exp3_baseline/records.jsonl.gz", "Raw ballot states, baseline walks."),
        ("runs/exp3_copycat/records.jsonl.gz", "Raw ballot states, copycat walks."),
        ("runs/exp3_escalation/records.jsonl.gz", "Raw ballot states, escalation walks."),
        ("runs/exp3_baseline/measures.csv", "Shared measures, baseline walks."),
    ]),
    ("Cross-experiment checks", [
        ("runs/summary_measures.md", "Shared measures across Experiments 1–3."),
        ("paradox_summary.md", "Monotonicity (more votes, fewer seats) search across every rule."),
        ("paradox_results.csv", "Every perturbation tested in the paradox search."),
    ]),
]

SCRIPTS = [
    "model.py", "model_2026.py", "model_levelling.py", "model_straight_ticket.py",
    "mc_overhang.py", "mc_analyse.py", "mc_history.py", "calibrate_history.py", "abc_history.py",
    "mc_calibrated.py", "mc_future.py", "futures_reason.py", "mc_future_walks.py", "mc_future_floor.py",
    "measures.py", "analyse_measures.py", "mc_paradox.py", "run_all_measures.sh", "build_site.py",
]


def release_only(path):
    from fnmatch import fnmatch
    return any(fnmatch(path, pat) for pat in RELEASE_ONLY)


def file_url(path):
    if not REPO_URL:
        return None
    if release_only(path):
        return f"{REPO_URL}/releases/latest"
    kind = "tree" if path.endswith("/") else "blob"
    return f"{REPO_URL}/{kind}/{BRANCH}/{path.rstrip('/')}"


def human_size(path):
    p = ROOT / path
    if p.is_dir():
        n = sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
    elif p.exists():
        n = p.stat().st_size
    else:
        return None
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


# ------------------------------------------------------------------- shared UI
NAV_ITEMS = [("index.html", "2023"), ("2026/index.html", "2026"),
             ("report/index.html", "Full report"), ("data/index.html", "Data &amp; code")]


def rel(from_out, to_out):
    """Relative link between two output paths under docs/."""
    depth = from_out.count("/")
    target = to_out[:-len("index.html")] if to_out.endswith("index.html") else to_out
    return ("../" * depth + target) or "./"


def nav(out, current):
    links = "".join(
        f'<a href="{rel(out, href)}"{" aria-current=\"page\"" if label == current else ""}>{label}</a>'
        for href, label in NAV_ITEMS)
    return f"""<nav class="sx-nav" aria-label="Site">
  <a class="sx-brand" href="{rel(out, 'index.html')}">One ballot, counted twice</a>
  <div class="sx-links">{links}</div>
</nav>"""


NAV_CSS = """
.sx-nav { max-width: 1120px; margin: 0 auto; display: flex; flex-wrap: wrap; align-items: center;
  justify-content: space-between; gap: 6px 20px; padding: 12px 0; border-bottom: 1px solid var(--line);
  font-family: var(--body); font-size: 15px; }
.sx-brand { font-family: var(--display); font-weight: 800; text-decoration: none; letter-spacing: -.01em; }
.sx-links { display: flex; flex-wrap: wrap; gap: 4px 18px; }
.sx-links a { color: var(--muted); text-decoration: none; font-weight: 600; }
.sx-links a:hover, .sx-links a[aria-current] { color: var(--ink); text-decoration: underline; text-underline-offset: 4px; }
"""

DEEPER = """<section class="sx-deeper" aria-labelledby="sx-deeper-h">
  <div>
    <p class="eyebrow">Go deeper</p>
    <h2 id="sx-deeper-h">The full analysis</h2>
  </div>
  <div class="sx-cards">
    <a class="sx-card" href="{report}">
      <h3>Read the report</h3>
      <p>Costs and benefits of the transfer and the alternatives, tested on 2005–2026 elections, 5,000 synthetic elections, and 1,000 simulated futures.</p>
    </a>
    <a class="sx-card" href="{other}">
      <h3>{other_label}</h3>
      <p>{other_text}</p>
    </a>
    <a class="sx-card" href="{data}">
      <h3>Data and code</h3>
      <p>The simulation outputs, the raw ballot states behind them, and the scripts that produce every number.</p>
    </a>
  </div>
</section>
"""

DEEPER_CSS = """
.sx-deeper { max-width: 1120px; margin: 0 auto; padding-block: 8px 64px; display: grid; gap: 24px; }
.sx-deeper h2 { font-size: clamp(28px, 3.4vw, 40px); margin-top: 8px; }
.sx-cards { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.sx-card { display: grid; gap: 8px; align-content: start; padding: 20px; background: var(--card);
  border: 1px solid var(--line); border-radius: 10px; text-decoration: none; }
.sx-card:hover { border-color: var(--ink); }
.sx-card h3 { font-size: 21px; }
.sx-card h3::after { content: " →"; }
.sx-card p { color: var(--muted); font-size: 16px; }
"""


# ---------------------------------------------------------------- explainers
def build_explainer(src_name, out_name, desc, og_title, og_desc):
    src = (ROOT / "site" / src_name).read_text(encoding="utf-8")
    is_2026 = out_name.startswith("2026")
    deeper = DEEPER.format(
        report=rel(out_name, "report/index.html"), data=rel(out_name, "data/index.html"),
        other=rel(out_name, "index.html" if is_2026 else "2026/index.html"),
        other_label="The 2023 version" if is_2026 else "The 2026 version",
        other_text=("The same story with the 2023 final results: 2 overhang seats." if is_2026 else
                    "The same story with the 2026 preliminary count: 11 overhang seats."))
    assert src.count("<footer>") == 1, f"{src_name}: expected one <footer> to place the links before"
    src = src.replace("<footer>", deeper + "\n<footer>", 1)
    page = f"""<!doctype html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{desc}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<style>[hidden]{{display:none!important}} img{{max-width:100%}} body{{margin:0}}{NAV_CSS}{DEEPER_CSS}</style>
</head>
<body>
{nav(out_name, "2026" if is_2026 else "2023")}
{src}
</body>
</html>
"""
    write(out_name, page)


# ------------------------------------------------------------------- reports
PAGE_CSS = """
:root {
  --paper: #F2F5F4; --card: #FFFFFF; --ink: #121A17; --muted: #5A6862; --line: #D3DCD8;
  --accent: #0B57A4; --mark: #FFF4C2; --code: #E6ECE9;
  --display: "Archivo", "Helvetica Neue", Arial, sans-serif;
  --body: "Source Sans 3", system-ui, -apple-system, "Segoe UI", sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #0E1412; --card: #161E1B; --ink: #E7EEEA; --muted: #97A69F; --line: #2A3531;
    --accent: #7FB2EE; --mark: #3A3410; --code: #1F2925; color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #0E1412; --card: #161E1B; --ink: #E7EEEA; --muted: #97A69F; --line: #2A3531;
  --accent: #7FB2EE; --mark: #3A3410; --code: #1F2925; color-scheme: dark;
}
* { box-sizing: border-box; }
html { scroll-padding-top: 16px; }
body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--body);
  font-size: 18px; line-height: 1.6; padding-inline: max(16px, env(safe-area-inset-left, 0px)); }
a { color: var(--accent); text-underline-offset: 3px; }
.sx-brand { color: var(--ink); }
.layout { max-width: 1120px; margin: 0 auto; display: grid; gap: 40px; padding-block: 32px 80px;
  grid-template-columns: minmax(0, 1fr); }
@media (min-width: 1000px) { .layout { grid-template-columns: 240px minmax(0, 1fr); } }
.toc { font-size: 14px; line-height: 1.4; }
.toc-inner { position: sticky; top: 16px; max-height: calc(100vh - 32px); overflow: auto; padding-right: 8px; }
.toc p { font-size: 12px; letter-spacing: .12em; text-transform: uppercase; font-weight: 700; color: var(--muted); margin: 0 0 8px; }
.toc ul { list-style: none; margin: 0; padding: 0; }
.toc ul ul { padding-left: 12px; }
.toc li { margin: 6px 0; }
.toc a { color: var(--muted); text-decoration: none; }
.toc a:hover { color: var(--ink); }
.toc .group { margin-top: 24px; }
@media (max-width: 999px) { .toc-inner { position: static; max-height: none; }
  .toc details:not([open]) ul { display: none; } }
article { max-width: 760px; min-width: 0; }
article h1, article h2, article h3, article h4 { font-family: var(--display); line-height: 1.15; text-wrap: balance; }
article h1 { font-size: clamp(32px, 4.4vw, 48px); font-weight: 800; letter-spacing: -.015em; margin: 0 0 12px; }
article h1 + h3 { font-family: var(--body); font-weight: 400; font-size: 21px; color: var(--muted); margin-top: 0; }
article h2 { font-size: 28px; margin: 56px 0 12px; padding-top: 16px; border-top: 1px solid var(--line); }
article h3 { font-size: 21px; margin: 36px 0 8px; }
article h4 { font-size: 18px; margin: 28px 0 6px; }
article hr { border: 0; border-top: 1px solid var(--line); margin: 40px 0; }
article blockquote { margin: 20px 0; padding: 4px 18px; border-left: 3px solid var(--line); color: var(--muted); }
article code { font-size: .86em; background: var(--code); padding: .1em .35em; border-radius: 4px; overflow-wrap: anywhere; }
article pre { background: var(--code); padding: 14px; border-radius: 8px; overflow: auto; font-size: 14px; }
article pre code { background: none; padding: 0; }
article img { max-width: 100%; }
.table-wrap { overflow-x: auto; margin: 20px 0; border: 1px solid var(--line); border-radius: 8px; background: var(--card); }
table { border-collapse: collapse; font-size: 15px; line-height: 1.4; min-width: 100%; }
th, td { padding: 8px 12px; text-align: left; vertical-align: top; border-bottom: 1px solid var(--line); }
th { font-weight: 700; background: var(--code); }
tr:last-child td { border-bottom: 0; }
td { font-variant-numeric: tabular-nums; }
.draft { background: var(--mark); border-radius: 8px; padding: 12px 16px; font-size: 15px; margin-bottom: 28px; }
.pager { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 16px; margin-top: 56px;
  padding-top: 20px; border-top: 1px solid var(--line); font-weight: 600; }
.foot { color: var(--muted); font-size: 14px; margin-top: 24px; }
.meta { color: var(--muted); }
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800'
         '&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap">')


def shell(out, title, desc, current, body):
    return f"""<!doctype html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
{FONTS}
<style>{PAGE_CSS}{NAV_CSS}</style>
</head>
<body>
{nav(out, current)}
{body}
</body>
</html>
"""


def link_code_spans(body, out):
    """Turn `file.md` / `data.csv` code spans into links: reports to their page, other files to GitHub."""
    pages = {src: dst for src, dst, _ in REPORTS}

    def sub(m):
        name = html.unescape(m.group(1))
        if name in pages:
            return f'<a href="{rel(out, pages[name])}">{m.group(0)}</a>'
        if (ROOT / name).exists() and (url := file_url(name)):
            return f'<a href="{url}">{m.group(0)}</a>'
        return m.group(0)

    return re.sub(r"<code>([\w./\-]+)</code>", sub, body)


LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s")


def gfm_compat(text):
    """Python-Markdown needs a blank line before a list and 4-space nesting; GitHub doesn't.
    Patch both so the reports render as they do on GitHub, without touching the sources."""
    out, prev, fenced = [], "", False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced:
            m = LIST_ITEM.match(line)
            if m and 0 < len(m.group(1)) < 4:
                line = "    " + line.lstrip()
            if m and prev.strip() and not LIST_ITEM.match(prev) and not prev.startswith(" ") and not m.group(1):
                out.append("")
        out.append(line)
        prev = line
    return "\n".join(out) + "\n"


def build_reports():
    built = []
    for src, out, short in REPORTS:
        path = ROOT / src
        if not path.exists():
            print(f"skip {src}: not found")
            continue
        text = gfm_compat(path.read_text(encoding="utf-8"))
        md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc", "attr_list"],
                               extension_configs={"toc": {"toc_depth": "2-3", "permalink": False}})
        body = md.convert(text)
        m = re.search(r"<h1[^>]*>(.*?)</h1>", body)
        title = re.sub("<[^>]+>", "", m.group(1)) if m else short
        first_p = re.search(r"<p>(.*?)</p>", body, re.S)
        desc = re.sub("<[^>]+>", "", first_p.group(1))[:220] if first_p else title
        body = re.sub(r"<table>", '<div class="table-wrap"><table>', body).replace("</table>", "</table></div>")
        body = link_code_spans(body, out)
        built.append((src, out, short, title, desc, body, md.toc_tokens, path.stat().st_mtime))

    for i, (src, out, short, title, desc, body, toc_tokens, mtime) in enumerate(built):
        sections = [t for t in toc_tokens for t in ([t] if t["level"] > 1 else t["children"])]
        toc_items = "".join(
            f'<li><a href="#{t["id"]}">{t["name"]}</a></li>' for t in sections if t["level"] == 2) or ""
        others = "".join(
            f'<li><a href="{rel(out, o)}"{" aria-current=\"page\"" if o == out else ""}>{s}</a></li>'
            for _, o, s, *_ in built)
        updated = dt.date.fromtimestamp(mtime).strftime("%-d %B %Y")
        src_link = (f'<a href="{file_url(src)}"><code>{src}</code></a>' if file_url(src) else f"<code>{src}</code>")
        prev_link = (f'<a href="{rel(out, built[i-1][1])}">← {built[i-1][2]}</a>' if i else "<span></span>")
        next_link = (f'<a href="{rel(out, built[i+1][1])}">{built[i+1][2]} →</a>' if i + 1 < len(built) else "")
        page_body = f"""<div class="layout">
<aside class="toc"><div class="toc-inner">
  <details open><summary class="meta" style="cursor:pointer;margin-bottom:8px">Contents</summary>
  <ul>{toc_items}</ul></details>
  <div class="group"><p>Report and appendices</p><ul>{others}</ul></div>
</div></aside>
<article>
<p class="draft"><strong>Working draft.</strong> Last updated {updated}. The analysis is still being refined and figures may change as simulations are rerun.</p>
{body}
<nav class="pager" aria-label="Report pages">{prev_link}{next_link}</nav>
<p class="foot">Generated from {src_link}. This describes proposals for discussion, not current electoral law.</p>
</article>
</div>"""
        write(out, shell(out, title, desc, "Full report", page_body))


# ---------------------------------------------------------------------- data
def build_data_page():
    out = "data/index.html"
    groups = []
    for heading, items in DATASETS:
        rows = []
        for path, what in items:
            size = human_size(path)
            if size is None:
                print(f"data page: {path} missing, left out")
                continue
            url = file_url(path)
            name = f'<a href="{url}"><code>{path}</code></a>' if url else f"<code>{path}</code>"
            where = "Release download" if release_only(path) else "In repository"
            rows.append(f"<tr><td>{name}</td><td>{what}</td><td>{size}</td><td>{where}</td></tr>")
        if rows:
            groups.append(f'<h2 id="{re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")}">{heading}</h2>'
                          '<div class="table-wrap"><table><thead><tr><th>File</th><th>Contents</th><th>Size</th>'
                          f'<th>Where</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>')

    script_rows = []
    for name in SCRIPTS:
        p = ROOT / name
        if not p.exists():
            continue
        if p.suffix == ".py":
            doc = ast.get_docstring(ast.parse(p.read_text(encoding="utf-8"))) or ""
            first = doc.strip().split("\n\n")[0].replace("\n", " ")
        else:
            lines = [l[1:].strip() for l in p.read_text().splitlines()[1:] if l.startswith("#")]
            first = lines[0] if lines else ""
        url = file_url(name)
        nm = f'<a href="{url}"><code>{name}</code></a>' if url else f"<code>{name}</code>"
        script_rows.append(f"<tr><td>{nm}</td><td>{html.escape(first)}</td></tr>")

    release = (f'<a href="{REPO_URL}/releases/latest">latest release</a>' if REPO_URL else "latest release")
    repo = (f'<a href="{REPO_URL}">GitHub repository</a>' if REPO_URL else "GitHub repository")
    body = f"""<div class="layout">
<aside class="toc"><div class="toc-inner"><p>On this page</p><ul>
{"".join(f'<li><a href="#{re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-")}">{h}</a></li>' for h, _ in DATASETS)}
<li><a href="#code">Code</a></li><li><a href="#reproduce">Reproducing the results</a></li></ul></div></aside>
<article>
<h1>Data and code</h1>
<p>Everything behind the <a href="{rel(out, 'report/index.html')}">report</a> is in the {repo}. Summary results and inputs are committed
directly. The raw ballot states and per-run measures are too large for the repository, so they are attached to the {release} as a single download.</p>
<p class="draft"><strong>Working draft.</strong> Built {TODAY.strftime("%-d %B %Y")}. Simulations are still being rerun, so files may change.</p>
{"".join(groups)}
<h2 id="code">Code</h2>
<p>Python 3, standard library and NumPy. Each script's docstring explains how to run it.</p>
<div class="table-wrap"><table><thead><tr><th>Script</th><th>What it does</th></tr></thead><tbody>{"".join(script_rows)}</tbody></table></div>
<h2 id="reproduce">Reproducing the results</h2>
<p><code>run_all_measures.sh</code> reruns Experiments 1–3, stores the raw ballot states in <code>runs/</code>, and computes every shared measure from them.
The full run takes several hours. <code>analyse_measures.py</code> then rebuilds the summary tables.</p>
<p class="foot">Election data: <a href="https://www.electionresults.govt.nz/">Electoral Commission</a>. Seats are allocated with the Sainte-Laguë formula used in New Zealand elections.</p>
</article></div>"""
    write(out, shell(out, "Data and code", "Simulation outputs, raw ballot states and scripts behind the overhang reform analysis.",
                     "Data &amp; code", body))


def write(out_name, text):
    out = DOCS / out_name
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    for args in PAGES:
        build_explainer(*args)
    build_reports()
    build_data_page()
    (DOCS / ".nojekyll").touch()
