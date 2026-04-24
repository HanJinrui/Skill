for _ in range(int(input())):
	(x, *a) = map(int, input().split())
	a.sort()
	print((x - 1) * a[0] + a[1])
