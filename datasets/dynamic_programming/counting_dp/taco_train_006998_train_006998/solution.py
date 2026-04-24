from math import *
(n, m, k) = map(int, input().split())
c = lambda n, k: 0 if k > n else factorial(n) // (factorial(k) * factorial(n - k))
print(c(n - 1, 2 * k) * c(m - 1, 2 * k) % 1000000007)
