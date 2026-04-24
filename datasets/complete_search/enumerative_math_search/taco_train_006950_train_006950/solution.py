for _ in range(int(input())):
	(n, r) = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	(c, d) = ([b[0]], b[0])
	for i in range(1, n):
		d = max(0, d - (a[i] - a[i - 1]) * r)
		d += b[i]
		c += [d]
	print(max(c))
