data = open("1.txt").read()
arr = [(ch, ops.split(",")) for line in data.splitlines() for ch, ops in [line.split(":")]]
ans = dict()
for ch, ops in arr:
    start, score = 10, 0
    for i in range(10):
        op = ops[i % len(ops)]
        match op:
            case "+":
                start += 1
            case "-":
                start -= 1
            case _:
                pass
        score += start
    ans[ch] = score

ans = sorted(ans.items(), key=lambda item: -item[1])
print("".join(x[0] for x in ans))
