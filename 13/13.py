import heapq

def dijkstra(start, end, maze):
    valid = {(r, c) for r in range(len(maze)) for c in range(len(maze[r])) if maze[r][c] != "#"}
    dists = {(r, c): float('inf') for r in range(len(maze)) for c in range(len(maze[r]))} 
    Q = [(0, start)]
    seen = set()
    while Q:
        cost, (r, c) = heapq.heappop(Q)
        if (r, c) in end:
            return cost
        if (r, c) in seen: continue
        seen.add((r, c))
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = dr+r, dc+c
            if (rr, cc) not in valid or (rr, cc) in seen:
                continue
            a, b = int(maze[r][c]), int(maze[rr][cc])
            height = min(abs(a - b), abs(a - b + 10), abs(a - b - 10))
            new_cost = cost + height + 1
            if new_cost < dists[(rr, cc)]:
                heapq.heappush(Q, (new_cost, (rr, cc)))
                dists[(rr, cc)] = new_cost
    return None

def parse(f):
    maze = [list(row) for row in open(f).read().splitlines()]
    start, end = [], []
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] not in "SE": continue
            if maze[r][c] == "S": start.append((r, c))
            if maze[r][c] == "E": end.append((r, c))
            maze[r][c] = 0
    return start, end, maze

def solve1():
    start, end, maze = parse("1.txt")
    return dijkstra(start[0], end, maze)

def solve2():
    start, end, maze = parse("2.txt")
    return dijkstra(start[0], end, maze)

def solve3():
    start, end, maze = parse("3.txt")
    return dijkstra(end[0], start, maze)
    
print(solve1(), solve2(), solve3())
