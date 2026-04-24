(n, k) = map(int, input().split())
k = min(k, n >> 1)
print(k * (n - k << 1) - k)
