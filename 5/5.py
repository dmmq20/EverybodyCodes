from collections import deque, defaultdict

def parse(f):
    data = open(f).read()
    data = [[int(n) for n in row.split(" ")] for row in data.splitlines()]
    data = deque((deque(l) for l in zip(*data)))
    return data

def clap(data, i):
    n = data[i%len(data)].popleft()
    m = len(data[(i+1)%len(data)]) # + 1
    if n % m == 0:
        if (n // m) % 2 == 1:
            data[(i+1)%len(data)].insert(-1, n)
        else:
            data[(i+1)%len(data)].insert(1, n)
    else:
        if (n // m) % 2 == 1:
            pos = n % m
            if pos == 1:
                data[(i+1)%len(data)].append(n)
            else:
                pos = -(pos - 1)
                data[(i+1)%len(data)].insert(pos, n)
        else: 
            pos = (n % m) - 1
            data[(i+1)%len(data)].insert(pos, n)
    k = int("".join(str(row[0]) for row in data))
    return k

def solve1():
    data = parse("1.txt")
    ans = [clap(data, i) for i in range(10)][-1]
    return ans

def solve2():
    data = parse("2.txt")
    ans = defaultdict(int)
    i = 0
    while True:
        k = clap(data, i)
        i += 1
        ans[k] += 1
        if ans[k] == 2024:
            break
    return k * i

def solve3():
    data = parse("3.txt")
    i = 0
    best = 0
    while i < 10_000:
        best = max(best, clap(data, i))
        i += 1
    return best

print(solve1())
print(solve2())
print(solve3())
