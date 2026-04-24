for _ in range(int(input())):
	(n, m) = map(int, input().split())
	d = {}
	for f in range(n):
		(a, b) = map(int, input().split())
		d[a] = max(d.get(a, 0), b)
	e = sorted(d.values())
	print(e[-1] + e[-2])
