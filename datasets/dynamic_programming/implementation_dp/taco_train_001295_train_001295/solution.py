for _ in range(int(input())):
	(n, m) = (int(input()), [input(), input()])
	x = 0
	for i in range(n):
		if int(m[x][i]) > 2:
			x ^= 1
			if int(m[x][i]) <= 2:
				x = 0
				break
	print('NO') if x == 0 else print('YES')
