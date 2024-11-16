def dp(beetles, stamps):
    dp = [float('inf')] * (max(beetles) + 1)
    dp[0] = 1
    for stamp in stamps:
        dp[stamp] = 1
        for i in range(stamp, len(dp)):
            dp[i] = min(dp[i], dp[i-stamp] + 1)

    return dp

def solve1():
    data = open("1.txt").read()
    beetles = [int(n) for n in data.splitlines()]
    stamps = [1, 3, 5, 10]
    counts = dp(beetles, stamps)
    return sum(counts[x] for x in beetles)

def solve2():
    data = open("2.txt").read()
    beetles = [int(n) for n in data.splitlines()]
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    counts = dp(beetles, stamps)
    return sum(counts[x] for x in beetles)

def solve3():
    data = open("3.txt").read()
    beetles = [int(n) for n in data.splitlines()]
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    counts = dp(beetles, stamps)
    total = 0
    for beetle in beetles:
        k = (beetle//2)
        ans = float('inf')
        for i in range(k-49, k+50):
            j = beetle - i
            ans = min(ans, counts[i] + counts[j])
        total += ans

    return (total)

print(solve1())
print(solve2())
print(solve3())
