from collections import deque

def parse(f):
    data = open(f).read().splitlines()
    palms = {(r, c) for r in range(len(data)) for c in range(len(data[r])) if data[r][c] == "P"}
    tree_dists = {(r, c): 0 for r in range(len(data)) for c in range(len(data[r]))  if data[r][c] == "."}

    return data, palms, tree_dists

def bfs(data, start, tree_dists):
    Q = deque([(0, *start)])
    seen = set()
    while Q:
        dist, r, c = Q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if data[r][c] != "P":
            tree_dists[(r, c)] += dist

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = dr+r, dc+c
            if 0<=rr<len(data) and 0<=cc<len(data[0]):
                if data[rr][cc] == "#": continue
                Q.append((dist+1, rr, cc))

    return None

def solve3():
    data, palms, tree_dists = parse("3.txt")
    for p in palms:
        bfs(data, p, tree_dists)
    return min(tree_dists.values())

print(solve3())
