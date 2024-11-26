from collections import Counter
import math

turns, rest = open("2.txt").read().split("\n\n")
turns = [int(n) for n in turns.split(",")]
machine = []

for row in rest.splitlines():
    k = ptr = 0
    while ptr < len(row):
        if len(machine) <= k:
            machine.append([])
        chunk = row[ptr:ptr+4].strip()
        if chunk:
            machine[k].append(row[ptr:ptr+4])
        ptr += 4
        k += 1

def get_nth_pull(n):
    s = ""
    for i, k in enumerate(turns):
        idx = (k * n) % len(machine[i])
        s += machine[i][idx][0] + machine[i][idx][2]
    return s

total = 0
totals = dict()
PULLS = 202420242024
lcm = math.lcm(*[len(w) for w in machine])
k = 1
while k <= lcm:
    s = get_nth_pull(k)
    total += sum(1 + x - 3 for x in Counter(s).values() if x > 2)
    totals[k] = total
    k += 1

print(totals[lcm] * (PULLS//lcm) + totals[PULLS%lcm])



