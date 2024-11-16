def parse(f):
    data = []
    for lines in open(f).read().split("\n\n"):
        temp = []
        for line in lines.splitlines():
            for i, chunk in enumerate(line.split(" ")):
                if i < len(temp):
                    temp[i].append(list(chunk))
                else:
                    temp.append([list(chunk)])
        data += temp
    return data

def solve(data):
    ans = []
    for row in data:
        for j in range(len(row)):
            if row[j] != ".":
                continue
            col = [data[k][j] for k in range(len(data))]
            x = (set(row) & set(col)) - {"."}
            if x:
                ans.append(x.pop())
    return "".join(ans)

def f(ans):
    return sum((i+1) * (ord(ans[i]) - ord('A') + 1) for i in range(len(ans)))

def solve1():
    data = parse("1.txt")
    return solve(data[0])

def solve2():
    return sum(f(solve(s)) for s in parse("2.txt"))

print(solve1())
print(solve2())
