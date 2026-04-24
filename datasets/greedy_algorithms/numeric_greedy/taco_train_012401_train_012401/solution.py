(n, c1) = (int(input()), input().split().count('1'))
v = min(c1, n - c1)
print(v + (c1 - v) // 3)
