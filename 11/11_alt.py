from collections import defaultdict

def parse(f):
    D = {}
    for line in open(f).read().strip().splitlines():
        src, dest = line.split(":")
        D[src] = dest.split(",")
    return D

def solve(start, days, D):
    ans = {start: 1}
    for _ in range(days):
        new = defaultdict(int)
        for k, v in ans.items():
            for c in D[k]:
                new[c] += v
        ans = new
    return sum(ans.values())

def solve3():
    D = parse("3.txt")
    ans = sorted([solve(k, 20, D) for k in D.keys()])
    return max(ans) - min(ans)

def solve2():
    D = parse("2.txt")
    return solve("Z", 10, D)

def solve1():
    D = parse("1.txt")
    return solve("A", 4, D)

print(solve1(), solve2(), solve3())
