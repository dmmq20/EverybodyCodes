from collections import defaultdict, Counter

s = [list(row) for row in open("3.txt").read().strip().splitlines()]
valid = {(r, c) for r in range(len(s)) for c in range(len(s[r])) if s[r][c] != " "}

Q, seen = [(0, 1)], {(0, 0)}
track = ""
while Q:
    r, c = Q.pop()
    if ((r, c)) in seen: continue
    seen.add((r, c))
    track += s[r][c]
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1 ,0)]:
        if (r+dr, c+dc) in valid:
            Q.append((r+dr, c+dc))
track += "="

def solve(arr):
    ans = defaultdict(int)
    for ch, ops in arr:
        power, score, i = 10, 0, 0
        for _ in range(11):
            for op in track: 
                if op in ["=", "S"]:
                    op = ops[i % len(ops)]
                i += 1
                match op:
                    case "+": power += 1
                    case "-": power -= 1
                    case _: assert op == "="
                score += power
        ans[ch] = score * 184
    return ans

data = """A:-,=,-,+,+,+,+,=,+,=,-"""
arr = [(ch, ops.split(",")) for line in data.strip().splitlines() for ch, ops in [line.split(":")]]

def check_winner(plan):
    ans = solve(arr + plan)
    ans = sorted(ans.items(), key=lambda item: -item[1])
    return ans[0][0]

def generate_unique_plans(counter):
    if sum(counter.values()) == 0:
        yield ""
        return

    for ch in counter:
        if counter[ch] > 0:
            counter[ch] -= 1
            for perm in generate_unique_plans(counter):
                yield ch + perm
            counter[ch] += 1

total = 0
counter = Counter({"+": 5, "-": 3, "=": 3})
for p in generate_unique_plans(counter):
    total += check_winner([("B", p)]) == "B"
print(total)
