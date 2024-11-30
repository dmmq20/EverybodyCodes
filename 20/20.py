from collections import defaultdict
import functools

@functools.cache
def solve(cur_pos, prev, time=0, alt=1000):
    
    r, c = cur_pos
    alt += ALT_DIFFS[data[r][c]]
    if time == 100:
        return alt
    if times[(time, cur_pos)] > alt:
        return 0
    times[(time, cur_pos)] = alt
    ret = 0
    for dr, dc in adj:
        rr, cc = dr+r, dc+c
        if (rr, cc) == prev: continue
        if not (0 <= rr < len(data)): continue
        if data[rr][cc] == "#": continue
        ret = max(ret, solve((rr, cc), cur_pos, time+1, alt))
        
    return ret

data = open("1.txt").read().splitlines()
start = (0, data[0].index("S"))
ALT_DIFFS = {".": -1, "-": -2, "+": 1, "S": 0}
adj = [(0,1), (0, -1), (1, 0), (-1, 0)]
times = defaultdict(int)

print(solve(start, start))
