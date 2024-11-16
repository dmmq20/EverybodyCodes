def parse(f):
    data = open(f).read().replace(".", "0").replace("#", "1")
    data = [[int(n) for n in line] for line in data.splitlines()]
    return data

def solve(area, depth, adj):
    change = False
    for r in range(len(area)):
        for c in range(len(area[r])):
            if area[r][c] == 0: continue
            if all(area[r+dr][c+dc] >= depth-1 for dr, dc in adj):
                change = True
                area[r][c] = depth
                
    return change

def solve1():
    data = parse("1.txt")
    k = 2
    while solve(data, k, [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        k += 1
    return sum(sum(r) for r in data)

def solve2():
    data = parse("2.txt")
    k = 2
    while solve(data, k, [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        k += 1
    return sum(sum(r) for r in data)

def solve3():
    data = parse("3.txt")
    data = [[0] + row + [0] for row in data]
    data.insert(0, [0] * len(data[0]))
    data.append([0] * len(data[0]))
    k = 2
    while solve(data, k, [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]):
        k += 1
    return sum(sum(r) for r in data)

print(solve1())
print(solve2())
print(solve3())


