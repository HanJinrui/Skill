for _ in range(int(input())):
	(n, x) = list(map(int, input().split()))
	a = n
	b = n
	f = 1
	while a > 0:
		if a == x:
			f = 0
			print(b)
			break
		b += b & -b
		a &= b
	if x == 0:
		print(b)
	elif f:
		print(-1)
