for t in range(int(input())):
	(m, n) = map(int, input().split())
	print(1)
	l = 0
	for i in range(1, n):
		a = (m - 1) % (i + 1)
		if l >= a:
			l = l + 1
		print(l + 1)
