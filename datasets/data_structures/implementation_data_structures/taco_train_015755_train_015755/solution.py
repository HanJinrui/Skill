I = lambda : map(int, input().split())
for i in range(int(input())):
	(n, m) = I()
	(a, b) = (list(I()), list(I()))
	(l, q, w) = ([0] * (n + 1), 0, 0)
	for i in range(n):
		l[a[i]] = i
	for i in b:
		o = l[i]
		if o > q:
			m += (o - w) * 2
			q = o
		w += 1
	print(m)
