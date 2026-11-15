#!/usr/bin/env python3
"""Plan commit counts per day so the GitHub contribution grid spells a word.
Letters = LETTER_COMMITS, background = deterministic 1..3. Usage: grid.py [--json]"""
import datetime as dt, json, random, sys

WORD = "Tohraan"
LETTER_COMMITS = 40
GLYPHS = {  # 5 wide x 7 tall
 "T": ["#####","..#..","..#..","..#..","..#..","..#..","..#.."],
 "o": [".....",".....",".###.","#...#","#...#","#...#",".###."],
 "h": ["#....","#....","#.##.","##..#","#...#","#...#","#...#"],
 "r": [".....",".....","#.##.","##..#","#....","#....","#...."],
 "a": [".....",".....",".###.","....#",".####","#...#",".####"],
 "n": [".....",".....","#.##.","##..#","#...#","#...#","#...#"],
}
def window(today):
    # GitHub grid: columns are weeks starting Sunday, last column holds today
    sunday = today - dt.timedelta(days=(today.weekday() + 1) % 7)
    start = sunday - dt.timedelta(weeks=52)
    return start, 53

def plan(today):
    start, ncols = window(today)
    cols = []
    for i, ch in enumerate(WORD):
        if i: cols.append([0]*7)
        g = GLYPHS[ch]
        cols += [[1 if g[r][c] == "#" else 0 for r in range(7)] for c in range(5)]
    off = (ncols - len(cols)) // 2
    rng = random.Random("tohraan-grid")
    days = {}
    for c in range(ncols):
        for r in range(7):
            d = start + dt.timedelta(weeks=c, days=r)
            if d > today: continue
            lit = 0 <= c-off < len(cols) and cols[c-off][r]
            days[d.isoformat()] = (LETTER_COMMITS if lit else rng.randint(1, 3), bool(lit))
    return start, ncols, days

if __name__ == "__main__":
    today = dt.date.today()
    start, ncols, days = plan(today)
    if "--json" in sys.argv:
        print(json.dumps({k: v[0] for k, v in days.items()}, indent=1)); sys.exit()
    for r in range(7):
        print("".join(("#" if days.get((start+dt.timedelta(weeks=c, days=r)).isoformat(), (0, False))[1] else ".") for c in range(ncols)))
    tot = sum(v[0] for v in days.values())
    print(f"\nwindow {start}..{today} | days {len(days)} | lit {sum(v[1] for v in days.values())} | commits {tot}")
