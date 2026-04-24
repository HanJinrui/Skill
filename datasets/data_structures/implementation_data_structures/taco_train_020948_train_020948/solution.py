(n, t) = map(int, input().split())
a = list(map(int, input().split()))
(b, c) = ([], [])
u = a[0]
for v in a[1:]:
	b.append(u)
	if v > u:
		(u, v) = (v, u)
	c.append(v)
for _ in range(t):
	x = int(input())
	if x < n:
		print(b[x - 1], a[x])
	else:
		print(u, c[(x - 1) % (n - 1)])
