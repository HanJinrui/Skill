t = [tuple(map(int, input().split())) for i in range(int(input()))]
print((max((2 * x + len(bin(y - 1)) for (x, y) in t)) + 1) // 2 - 1)
