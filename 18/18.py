from collections import deque

def parse(f):
    data = open(f).read().splitlines()
    palms = {(r, c) for r in range(len(data)) for c in range(len(data[r])) if data[r][c] == "P"}
    return data, palms

def bfs(data, palms, start):
    Q = deque(start)
    seen = set()
    while Q:

        dist, r, c = Q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if data[r][c] == "P":
            palms.remove((r, c))
        if not palms:
            return dist

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = dr+r, dc+c
            if 0<=rr<len(data) and 0<=cc<len(data[0]):
                if data[rr][cc] == "#": continue
                Q.append((dist+1, rr, cc))

    return None

def solve1():
    data, palms = parse("1.txt")
    return bfs(data, palms, [(0, 1, 0)])

def solve2():
    data, palms = parse("2.txt")
    start = [(0, 1, 0), (0, len(data)-2, len(data[0])-1)]
    return bfs(data, palms, start)

print(solve1(), solve2())
