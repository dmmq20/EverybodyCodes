def parse(f):

    runes, s = open(f).read().split("\n\n")
    _, runes = runes.split(":")
    runes = runes.split(",")
    s = [line for line in s.splitlines()]

    return runes, s

def columns(s, runes, ans):
    for i in range(len(s)):
        line = "".join(s[i])
        for j in range(len(s[i])):
            for r in runes:
                dr = r[::-1]
                if line[j:].startswith(r) or line[j:].startswith(dr):
                    for idx in range(j, j+len(r)):
                        ans[idx][i] = 1
    return ans

def rows(s, runes, ans):
    for i in range(len(s)):
        for j in range(len(s[i])):
            for r in runes:
                dr = r[::-1]
                end = (j + len(r)) % len(s[i])
                idxs = []
                if end < j:
                    w = s[i][j:] + s[i][:end]
                    if w == r or w == dr:
                        idxs = list(range(j, len(s[i]))) + list(range(end))
                else:
                    w = s[i][j:j+len(r)]
                    if w == r or w == dr:
                        idxs = list(range(j, j+len(r)))
                for idx in idxs:
                    ans[i][idx] = 1
    return ans

def solve1():

    runes, s = parse("1.txt")
    ans = 0
    for line in s:
        for i in range(len(line)):
            for r in runes:
                if line[i:].startswith(r):
                    ans += 1
    return ans

def solve2():

    runes, s = parse("2.txt")
    total = 0
    for line in s:
        ans = [0] * len(line)
        for i in range(len(line)):
            for r in runes:
                if line[i:].startswith(r) or line[i:].startswith(r[::-1]):
                    for j in range(i, i+len(r)):
                        ans[j] = 1
        total += sum(ans)
    return total

def solve3():

    runes, s = parse("3.txt")
    ans = [[0] * len(r) for r in s]
    rows(s, runes, ans)
    columns(list(zip(*s)), runes, ans)
    ans = sum(sum(r) for r in ans)
    return ans

print(solve1())
print(solve2())
print(solve3())

