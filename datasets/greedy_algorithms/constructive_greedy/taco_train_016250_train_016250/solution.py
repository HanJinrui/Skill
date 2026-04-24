(n, m) = map(int, input().split())
n += 1
print(-1 if m < n - 2 or 2 * n < m else '0'.join(('1' * (m // n + (i % n < m % n)) for i in range(-1, n - 1))))
