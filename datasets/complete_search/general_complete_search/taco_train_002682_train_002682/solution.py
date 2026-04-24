t = int(input())
for z in range(t):
	(n, d) = map(int, input().split(' '))
	a = []
	a.append((n, 0))
	i = 0
	while i < 2048:
		y = []
		for j in str(a[i][0]):
			y.append(j)
		y = [int(k) for k in y]
		s = sum(y)
		a.append((s, a[i][1] + 1))
		a.append((a[i][0] + d, a[i][1] + 1))
		i = i + 1
	q = min(a)
	print(q[0], q[1])
