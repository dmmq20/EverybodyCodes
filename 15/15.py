import functools
from collections import deque

def parse(f):
    data = [list(row) for row in open(f).read().strip().splitlines()]
    idx = data[0].index(".")
    data[0][idx] = "S"
    plants = []
    start = None
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
            elif char.isalpha():
                plants.append((char, r, c))
    return data, start, plants

def bfs(start, data, targets):
    Q = deque([(0, start)])
    seen = {start}
    dists = []

    while targets:
        dist, (r, c) = Q.popleft()
        if (r, c) != start and (r, c) in targets:
            dists.append((dist, (r, c)))
            targets.remove((r, c))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rr, cc = r + dr, c + dc
            if (rr, cc) in seen: continue
            if 0 <= rr < len(data) and 0 <= cc < len(data[0]) and data[rr][cc] not in "#~":
                seen.add((rr, cc))
                Q.append((dist + 1, (rr, cc)))

    return dists

def build_distance_matrix(data, plants, start):
    positions = {(r, c) for _, r, c in plants}
    positions.add(start)
    D = {}
    for r, c in positions:
        D[(r, c)] = bfs((r, c), data, positions - {(r, c)})
    return D

def solve(start, need, D, maze, start_pos):
    @functools.lru_cache(maxsize=None)
    def f(pos, remaining):
        if not remaining:
            for dist, end_pos in D[pos]:
                if end_pos == start_pos:
                    return dist
            return float('inf')

        ans = float('inf')
        for dist, (r, c) in D[pos]:
            char = maze[r][c]
            if char in remaining:
                new_remaining = tuple(x for x in remaining if x != char)
                ans = min(ans, dist + f((r, c), new_remaining))
        return ans

    return f(start, tuple(need))

def solve1():
    data, start_pos, plants = parse("1.txt")
    D = build_distance_matrix(data, plants, start_pos)
    need = set(char for char, _, _ in plants) - {'S'}
    return solve(start_pos, need, D, data, start_pos)

def solve2():
    data, start_pos, plants = parse("2.txt")
    D = build_distance_matrix(data, plants, start_pos)
    need = set(char for char, _, _ in plants) - {'S'}
    return solve(start_pos, need, D, data, start_pos)

# VERY slow -- find optimization
def solve3():
    data, start_pos, plants = parse("3.txt")
    D = build_distance_matrix(data, plants, start_pos)
    need = set(char for char, _, _ in plants) - {'S'}
    return solve(start_pos, need, D, data, start_pos)

print(solve1(), solve2())
