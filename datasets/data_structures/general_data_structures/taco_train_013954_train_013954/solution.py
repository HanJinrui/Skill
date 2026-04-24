for i in range(int(input())):
	(r, c, k) = map(int, input().split())
	d = {}
	for j in range(k):
		(x, y) = map(int, input().split())
		d[x, y] = 4
		l = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
		for i in l:
			if i in d:
				d[x, y] -= 1
				d[i] -= 1
	print(sum(d.values()))
