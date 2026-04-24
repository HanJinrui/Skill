(n, m) = map(int, input().split())
D = [0] * (n + 2)
for _ in range(m):
	(a, b, k) = map(int, input().split())
	D[a] += k
	D[b + 1] -= k
for i in range(1, n + 1):
	D[i] += D[i - 1]
print(max(D))
