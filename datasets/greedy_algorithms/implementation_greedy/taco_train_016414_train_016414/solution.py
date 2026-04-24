(n, m, k) = map(int, input().split())
v = [1000000] * m
for i in range(n):
	(r, c) = map(int, input().split())
	v[r - 1] = min(v[r - 1], c)
print(min(sum(v), k))
