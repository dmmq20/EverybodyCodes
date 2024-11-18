from functools import cache

class Solve:
    def __init__(self, filename):
        self.D = self.parse(filename)
        self.f = cache(self._f)
    
    def parse(self, f):
        D = {}
        for line in open(f).read().strip().splitlines():
            a, b = line.split(":")
            D[a] = b.split(",")
        return D
    
    def _f(self, k, days):
        if days == 1:
            return len(self.D[k])
        return sum(self.f(v, days-1) for v in self.D[k])

def solve1():
    solve = Solve("1.txt")
    return solve.f("A", 4)

def solve2():
    solve = Solve("2.txt")
    return solve.f("Z", 10)

def solve3():
    solve = Solve("3.txt")
    ans = [solve.f(k, 20) for k in solve.D.keys()]
    return max(ans) - min(ans)

print(solve1(), solve2(), solve3())
