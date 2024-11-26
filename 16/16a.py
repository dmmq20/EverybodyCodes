turns, rest = open("1.txt").read().split("\n\n")
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
        s += machine[i][idx]
    return s

print(get_nth_pull(100))
