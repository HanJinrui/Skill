input()
a = [*map(int, input().split())]
m = min(a)
print(sum(a) - max((y + m - y // x - m * x for y in set(a) for x in range(1, int(y ** 0.5) + 1) if y % x == 0)))
