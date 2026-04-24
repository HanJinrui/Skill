for _ in range(int(input())):
	n = int(input())
	d = {}
	for i in range(3 * n):
		(x, y) = input().split()
		if x not in d:
			d.update({x: int(y)})
		else:
			d[x] += int(y)
	print(*sorted(d.values()))
