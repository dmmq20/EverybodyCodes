from collections import defaultdict

def parse(f):
    data = [list(row.strip()) for row in open(f).read().splitlines()]
    targets = {(r, c) for r in range(len(data)) for c in range(len(data[r])) if data[r][c] in ["T", "H"]}
    catapults = [(r, c) for r in range(len(data)) for c in range(len(data[r])) if data[r][c] not in ["T", ".", "=", "H"]]
    catapults.sort()
    return data, targets, catapults

def solve(data, targets, catapults):
    D = defaultdict(int)
    k = 1
    ans = 0
    while targets:
        hit = False
        for r, c in catapults:
            ch = data[r][c]
            r -= 1 * k
            c += 2 * k
            while r < len(data):
                if (r, c) in targets:
                    hit = True
                    ans += (k * (ord(ch) - ord("A") + 1))
                    if data[r][c] == "H":
                        D[(r, c)] += 1
                    if data[r][c] == "T" or D[(r, c)] == 2:
                        targets.remove((r, c))
                    break
                r += 1
                c += 1
        if not hit:
            k += 1
    return ans

def solve1():
    data, targets, catapults = parse("1.txt")
    return solve(data, targets, catapults)

def solve2():
    data, targets, catapults = parse("2.txt")
    return solve(data, targets, catapults)

print(solve1(), solve2())

