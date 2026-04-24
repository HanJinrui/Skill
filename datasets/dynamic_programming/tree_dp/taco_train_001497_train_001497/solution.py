for f in range(int(input())):
	n = int(input())
	p = [*map(int, input().split())]
	s = input()
	d = [0] * n
	for i in range(n - 1, -1, -1):
		d[i] += 1 if s[i] == 'W' else -1
		if i > 0:
			d[p[i - 1] - 1] += d[i]
	print(d.count(0))
