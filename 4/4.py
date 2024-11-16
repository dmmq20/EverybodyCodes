def parse(f):
    data = open(f).read()
    return sorted([int(n) for n in data.splitlines()])
    
def f(nails, m):
    return sum(abs(x-m) for x in nails)

def solve1():
    data = parse("1.txt")
    m = min(data)
    return f(data, m)

def solve2():
    data = parse("2.txt")
    m = min(data)
    return f(data, m)    

def solve3():
    data = parse("3.txt")
    m = data[len(data)//2]
    return f(data, m)

print(solve1())
print(solve2())
print(solve3())
