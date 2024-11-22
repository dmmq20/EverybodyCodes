from collections import deque

def bfs(start, leafs, segments):
    Q = deque([(0, start)])
    move = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    seen = set()
    ans = 0
    while leafs:
        dist, (x, y, z) = Q.popleft()
        if (x, y, z) in seen: continue
        seen.add((x, y, z))

        if (x, y, z) in leafs:
            ans += dist
            leafs.remove((x, y, z))

        for dx, dy, dz in move:
            xx, yy, zz = x+dx, y+dy, z+dz
            if (xx, yy, zz) in segments:
                Q.append((dist+1, (xx, yy, zz)))

    return ans

def grow(steps):
    segments = set()
    leafs = []
    for line in steps.strip().splitlines():
        x = y = z = 0
        for dir_ in line.split(","):
            d, n = dir_[:1], dir_[1:]
            for _ in range(int(n)):
                match d:
                    case "U": y += 1
                    case "D": y -= 1
                    case "R": x += 1
                    case "L": x -= 1
                    case "F": z += 1
                    case "B": z -= 1
                segments.add((x, y, z))
        leafs.append((x, y, z))
    return segments, leafs

def solve1():
    segments, _ = grow(open("1.txt").read())
    return max(y for _, y ,_ in segments)

def solve2():
    segments, _ = grow(open("2.txt").read())
    return len(segments)

def solve3():
    segments, leafs = grow(open("3.txt").read())
    trunk = [(x, y, z) for x, y, z in segments if x == z == 0]
    return min(bfs(t, leafs.copy(), segments) for t in trunk)

print(solve1(), solve2(), solve3())
