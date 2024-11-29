def parse(f):
    key, data = open(f).read().split("\n\n")
    data = [list(row) for row in data.strip().splitlines()]
    return data, key

def decode(data, key, repeat):
    adj = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    R, C = len(data), len(data[0])
    rot_points = [(r, c) for r in range(1, R-1) for c in range(1, C-1)]
    for _ in range(repeat):
        k = 0
        for r, c in rot_points:
            rot = key[k % len(key)]
            arr = [data[r+dr][c+dc] for dr, dc in adj]
            if rot == "L":
                arr = arr[1:] + [arr[0]]
            else:
                arr = [arr[-1]] + arr[:-1]
            for i, (dr, dc) in enumerate(adj):
                data[r+dr][c+dc] = arr[i]
            k += 1

    s = "".join("".join(row) for row in data)
    return s[s.index(">")+1:s.index("<")]

def solve1():
    data, key = parse("1.txt")
    return decode(data, key, 1)

def solve2():
    data, key = parse("2.txt")
    return decode(data, key, 100)

print(solve1(), solve2())
