(n, m) = map(int, input().split())
t = [n]
for i in range(1, n):
	t = t + [n - i] if m - 1 & 1 << i - 1 else [n - i] + t
for q in t:
	print(q)
