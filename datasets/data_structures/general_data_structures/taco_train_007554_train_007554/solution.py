(n, m) = map(int, input().split())
d1 = {}
for i in range(n):
	(a, b, c, d) = map(int, input().split())
	if (a, b) not in d1:
		d1[a, b] = [c, d]
	elif d1[a, b][1] <= d:
		d1[a, b] = [c, d]
for __ in range(m):
	(x, y) = map(int, input().split())
	print(d1[x, y][0])
