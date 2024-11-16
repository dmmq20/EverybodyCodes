from collections import defaultdict

def parse(f):

    data = open(f).read()
    G = defaultdict(list)
    for line in data.strip().splitlines():
        parent, children = line.split(":")
        G[parent] += children.split(",")

    return G
    
def f(G):
    Q = [("RR", ["RR"])]
    paths = defaultdict(list)

    while Q:
        node, path = Q.pop()
        if node in ["ANT", "BUG"]:
            continue
        if node == "@":
            paths[len(path)].append(path)
        
        for child in G[node]:
            Q.append((child, path+[child]))
    return paths

def solve1():

    G = parse("1.txt")
    paths = f(G)
    for ps in paths.values():
        if len(ps) == 1:
            return "".join(p for p in ps[0])

def solve2():

    G = parse("2.txt")
    paths = f(G)
    for ps in paths.values():
        if len(ps) == 1:
            return "".join(p[0] for p in ps[0])

def solve3():

    G = parse("3.txt")
    paths = f(G)
    for ps in paths.values():
        if len(ps) == 1:
            return "".join(p[0] for p in ps[0])

print(solve1())
print(solve2())
print(solve3())
