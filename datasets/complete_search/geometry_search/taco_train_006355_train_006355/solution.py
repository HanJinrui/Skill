f = lambda : map(int, input().split())
(n, r) = f()
(p, d) = ([], 2 * r)
for x in f():
	y = r
	for (a, b) in p:
		if abs(a - x) <= d:
			y = max(y, b + (d * d - (a - x) ** 2) ** 0.5)
	p.append((x, y))
for (x, y) in p:
	print(y)
