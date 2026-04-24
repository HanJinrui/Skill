(n, l, v1, v2, k) = map(int, input().split())
col = (n + k - 1) // k
m = l / (1 + 2 * (col - 1) * v1 / (v1 + v2))
print(m / v2 + (l - m) / v1)
