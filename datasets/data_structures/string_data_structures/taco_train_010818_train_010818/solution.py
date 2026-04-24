for q in range(int(input())):
	(l, h) = map(int, input().split())
	s = input()
	c = 0
	for i in s:
		if int(i) == 0:
			c += 1
		else:
			if 2 * c > h:
				h = 2 * (h - c)
			c = 0
		if h - c <= 0:
			break
	if h - c <= 0:
		print('YES')
	else:
		print('NO')
