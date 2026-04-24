(t, k) = map(int, input().split())
m = 1000000007
r = list(range(1, k + 1))
for i in range(k, 100001):
	r.append((r[i - 1] + r[i - k] + 1) % m)
for i in range(t):
	(a, b) = map(int, input().split())
	print((r[b] - r[a - 1]) % m)
