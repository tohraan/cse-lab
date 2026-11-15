"""Turns the problem bank into small, ordered commits (5 per problem).

Step k  ->  problem k // 5, stage k % 5:
  0 sketch the API (stub)   1 implement   2 add tests
  3 note complexity         4 index in README
"""
import ast
import pathlib
import subprocess

from problems import P

ROOT = pathlib.Path(__file__).resolve().parent.parent
STAGES = 5
TOTAL = len(P) * STAGES
TRAILER = "\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"


def stub(code: str) -> str:
    class T(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            doc = ast.get_docstring(node)
            node.body = ([ast.Expr(ast.Constant(doc))] if doc else []) + [
                ast.Raise(exc=ast.Name("NotImplementedError", ast.Load()), cause=None)]
            return node

    tree = ast.fix_missing_locations(T().visit(ast.parse(code)))
    return ast.unparse(tree) + "\n"


def doc(p, with_cx=False):
    s = f'"""{p["title"]}.'
    if with_cx:
        s += f'\n\nTopic: {p["topic"]} ({p["diff"]}).\nComplexity: {p["cx"]}.\n'
    return s + '"""\n\n'


def readme(done: int) -> str:
    rows = "\n".join(
        f'| {i + 1} | [{p["title"]}](cselab/{p["slug"]}.py) | {p["topic"]} | {p["diff"]} | {p["cx"]} |'
        for i, p in enumerate(P[:done]))
    return f"""# cse-lab

![tests](https://github.com/tohraan/cse-lab/actions/workflows/ci.yml/badge.svg)

Data structures, algorithms and systems building blocks in plain Python.
Every problem is built the same way: sketch the API, write the tests, implement, document the complexity.

```bash
pip install pytest
pytest -q
```

## Problems ({done})

| # | Problem | Topic | Difficulty | Complexity |
|---|---------|-------|------------|------------|
{rows}

## How this repo is built

Problems are released in small commits (`tools/stages.py`). A daily workflow
(`.github/workflows/drip.yml`) releases the next batch until the bank in
`tools/problems.py` runs out. The first commits were backfilled with
`tools/build_history.py`, so their dates are planned, not the day the code was
first typed. Everything after the backfill carries its real date.
"""


def apply_step(k: int, root: pathlib.Path = ROOT):
    """Write the files for step k; return (paths, commit message)."""
    p, stage = P[k // STAGES], k % STAGES
    src = root / "cselab" / f"{p['slug']}.py"
    test = root / "tests" / f"test_{p['slug']}.py"
    slug, title = p["slug"], p["title"]
    if stage == 0:
        src.write_text(doc(p) + stub(p["code"]))
        return [src], f"feat({slug}): sketch the {title} API"
    if stage == 1:
        src.write_text(doc(p) + p["code"])
        return [src], f"feat({slug}): implement {title}"
    if stage == 2:
        test.write_text(p["tests"])
        return [test], f"test({slug}): cover {title}"
    if stage == 3:
        src.write_text(doc(p, True) + p["code"])
        return [src], f"docs({slug}): note complexity of {title}"
    readme_path = root / "README.md"
    readme_path.write_text(readme(k // STAGES + 1))
    return [readme_path], f"docs: index {title} in the README"


def git(*args, env=None, root=ROOT):
    subprocess.run(["git", *args], cwd=root, check=True, env=env, capture_output=True)
