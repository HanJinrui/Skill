(n, k) = map(int, input().split())
print((n - 1) // k * 2 + min(2, (n - 1) % k))
for i in range(2, n + 1):
	print(i, max(i - k, 1))
