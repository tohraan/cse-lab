"""One-off backfill: replays the first N steps across the days that spell the word
in the contribution grid (see grid.py). Run once in a fresh repo."""
import datetime as dt
import os
import sys

import grid
from stages import ROOT, STAGES, TRAILER, apply_step, git

PER_DAY = 2
HOURS = [(10, 7), (15, 42)]
EMAIL = os.environ["GIT_EMAIL"]
NAME = os.environ.get("GIT_NAME", "Tohraan Ahmad Khan")

_, _, days = grid.plan(dt.date.today())
lit = sorted(d for d, (_, is_lit) in days.items() if is_lit)
n_steps = len(lit) * PER_DAY
print(f"{len(lit)} lit days x {PER_DAY} = {n_steps} commits")

SCAFFOLD = {
    "cselab/__init__.py": "",
    ".gitignore": "__pycache__/\n.pytest_cache/\n*.pyc\n.DS_Store\n",
    "pyproject.toml": '[project]\nname = "cse-lab"\nversion = "0.1.0"\nrequires-python = ">=3.9"\n\n[tool.pytest.ini_options]\npythonpath = ["."]\ntestpaths = ["tests"]\n',
    ".github/workflows/ci.yml": "name: ci\non: [push, pull_request]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.12'\n      - run: pip install pytest\n      - run: pytest -q\n",
}

git("init", "-q", "-b", "main")
(ROOT / "tests").mkdir(exist_ok=True)
for rel, text in SCAFFOLD.items():
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text)

for k in range(n_steps):
    paths, msg = apply_step(k)
    if k == 0:
        paths += [ROOT / r for r in SCAFFOLD]
        msg = "chore: scaffold cse-lab and sketch the first API"
    day = lit[k // PER_DAY]
    h, m = HOURS[k % PER_DAY]
    stamp = f"{day}T{h:02d}:{m:02d}:00+0000"
    env = dict(os.environ, GIT_AUTHOR_DATE=stamp, GIT_COMMITTER_DATE=stamp,
               GIT_AUTHOR_NAME=NAME, GIT_COMMITTER_NAME=NAME,
               GIT_AUTHOR_EMAIL=EMAIL, GIT_COMMITTER_EMAIL=EMAIL)
    git("add", *[str(p.relative_to(ROOT)) for p in paths], env=env)
    git("commit", "-q", "-m", msg + TRAILER, env=env)

(ROOT / "tools" / "state.json").write_text('{"released": %d}\n' % n_steps)
print("done", n_steps)
