def solve(chunks, rules):
    total = 0
    for chunk in chunks:
        k = len(chunk)
        if k == 0: continue
        total += sum(rules[ch] for ch in chunk) + k * (k - 1)
    
    return total

def part1():
    data = list(open("1.txt").read().strip())
    rules = {'A': 0, 'B': 1, 'C': 3}
    return solve(data, rules)

def part2():
    data = open("2.txt").read().strip()
    data = [data[i:i+2].replace("x", "") for i in range(0, len(data), 2)]
    rules = {'A': 0, 'B': 1, 'C': 3, 'D': 5}
    return solve(data, rules)

def part3():
    data = open("3.txt").read().strip()
    data = [data[i:i+3].replace("x", "") for i in range(0, len(data), 3)]
    rules = {'A': 0, 'B': 1, 'C': 3, 'D': 5}
    return solve(data, rules)

print(part1())
print(part2())
print(part3())
