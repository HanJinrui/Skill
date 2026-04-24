t = int(input())
for _ in range(t):
	(x, y, z) = list(map(int, input().split()))
	a = [[0] * z for _ in range(y)]
	for i in range(x):
		b = [0] * z
		for j in range(y):
			l = list(map(int, input().split()))
			print(l[0] - b[0] - a[j][0], end=' ')
			s = l[0] - b[0] - a[j][0]
			b[0] += s
			for k in range(1, z):
				e = l[k] - b[k] - a[j][k] - s
				print(e, end=' ')
				s += e
				b[k] += s
			print()
			a[j] = l
