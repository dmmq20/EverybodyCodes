import heapq, math

def parse(f):
    stars = set()
    for r, row in enumerate(open(f).read().splitlines()):
        for c, ch in enumerate(row):
            if ch == "*":
                stars.add((r, c))
    return stars

def prims(stars, max_dist=None):
    pq = [(0, stars.pop())]
    seen = set()
    ans = 0
    while pq:
        dist, (r, c) = heapq.heappop(pq)
        if (r, c) in seen:
            continue
        seen.add((r, c))
        ans += dist
        for dr, dc in stars:
            if (dr, dc) in seen:
                continue
            dist = abs(dr - r) + abs(dc - c)
            if not max_dist or dist < max_dist:
                heapq.heappush(pq, (dist, (dr, dc)))
    stars -= seen
    return ans + len(seen)

def solve1():
    stars = parse("1.txt")
    return prims(stars)

def solve2():
    stars = parse("2.txt")
    return prims(stars)

def solve3():
    constellations = []
    stars = parse("3.txt")
    while stars:
        constellations.append(prims(stars, 6))
    constellations.sort()
    return math.prod(constellations[-3:])

print(solve1(), solve2(), solve3())
