from math import comb as c
(n, m) = map(int, input().split())
print(c(n + 2 * m - 1, 2 * m) % 1000000007)
