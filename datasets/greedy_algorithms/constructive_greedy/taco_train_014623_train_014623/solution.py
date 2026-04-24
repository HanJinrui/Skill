(n, m) = sorted(map(int, input().split()))
k = 4 * (m >> 2)
print(m if n == 1 else k + 2 * min(2, m - k) if n == 2 else m * n + 1 >> 1)
