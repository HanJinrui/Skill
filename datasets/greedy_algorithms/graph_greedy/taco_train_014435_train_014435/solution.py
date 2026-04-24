n = int(input())
a = [0] * n
g = []
for _ in range(n - 1):
	(x, y) = map(int, input().split())
	x -= 1
	y -= 1
	a[x] += 1
	a[y] += 1
	g.append([x, y])
(m1, m2) = (0, n - 2)
for (x, y) in g:
	if a[x] == 1 or a[y] == 1:
		print(m1)
		m1 += 1
	else:
		print(m2)
		m2 -= 1
