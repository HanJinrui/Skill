(n, l, r) = map(int, input().split())
print(2 ** l - 1 + n - l, (2 + n - r) * 2 ** (r - 1) - 1)
