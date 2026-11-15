"""Release the next batch of bank commits with today's real date. Run by drip.yml."""
import json
import pathlib
import sys

from stages import ROOT, TOTAL, apply_step, git

PER_RUN = 5
state_file = ROOT / "tools" / "state.json"
state = json.loads(state_file.read_text())
start = state["released"]
if start >= TOTAL:
    print("bank empty - add problems to tools/problems.py")
    sys.exit(0)

end = min(start + PER_RUN, TOTAL)
for k in range(start, end):
    paths, msg = apply_step(k)
    if k == end - 1:
        state_file.write_text(json.dumps({"released": end}) + "\n")
        paths.append(state_file)
    git("add", *[str(p.relative_to(ROOT)) for p in paths])
    git("commit", "-q", "-m", msg)
print(f"released steps {start}..{end - 1}")
