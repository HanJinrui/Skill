for i in range(int(input())):
	(n, q) = map(int, input().split())
	a = [int(x) for x in input().split()]
	b = [0] * (n + 1)
	for j in range(n):
		if a[j] % 2 == 0:
			b[j + 1] = b[j]
		else:
			b[j + 1] = b[j] + 1
	for j in range(q):
		(l, r) = map(int, input().split())
		so = b[r] - b[l - 1]
		se = r - l + 1 - so
		s = se * (se - 1) * (se - 2) / 6 + se * so * (so - 1) / 2
		print(int(s))
