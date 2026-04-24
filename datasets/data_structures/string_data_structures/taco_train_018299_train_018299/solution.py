for _ in range(int(input())):
	(x, y) = map(int, input().split())
	a = 'a'
	b = 'b'
	(s1, s2) = ('', '')
	if x % 2 == 1 and y % 2 == 1:
		print(-1)
	elif x == 1 or y == 1:
		print(-1)
	else:
		if x % 2 == 1 and y % 2 == 0:
			s1 = b * (y // 2) + a * x + b * (y // 2)
			s2 = a + b * (y // 2) + a * (x - 2) + b * (y // 2) + a
		else:
			s1 = a * (x // 2) + b * y + a * (x // 2)
			s2 = b + a * (x // 2) + b * (y - 2) + a * (x // 2) + b
		print(s1)
		print(s2)
