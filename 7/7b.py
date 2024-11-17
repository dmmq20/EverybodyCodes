data, track_raw = open("2.txt").read().split("\n\n")
arr = [(ch, ops.split(",")) for line in data.strip().splitlines() for ch, ops in [line.split(":")]]
s = track_raw.strip().split('\n')

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

ans = dict()
for ch, ops in arr:
    power, score, i = 10, 0, 0
    for _ in range(10):
        for op in track: 
            if op == "=":
                op = ops[i % len(ops)]
            i += 1
            match op:
                case "+": power += 1
                case "-": power -= 1
                case _: assert op == "="
            score += power
    ans[ch] = score

ans = sorted(ans.items(), key=lambda item: -item[1])
print("".join(x[0] for x in ans))
