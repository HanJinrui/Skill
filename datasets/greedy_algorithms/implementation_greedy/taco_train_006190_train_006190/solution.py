(n, m) = map(int, input().split())
a = list(map(int, input().split()))
print(-1 if sum(a) < m else min(min(a), (sum(a) - m) // n))
