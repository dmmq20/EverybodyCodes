data, track_raw = open("2.txt").read().split("\n\n")
arr = [(ch, ops.split(",")) for line in data.strip().splitlines() for ch, ops in [line.split(":")]]
track_raw = track_raw.strip().split('\n')

track = ''
for i, row in enumerate(track_raw):
    if i == 0:
        track += row[1:]
    elif i == len(track_raw) - 1:
        track += row[::-1]
    else:
        track += row[-1]

for i, row in enumerate(track_raw):
    if 0 < i < len(track_raw) - 1:
        track += row[0]
track += '='

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
