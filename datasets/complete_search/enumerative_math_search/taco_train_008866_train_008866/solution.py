for i in range(int(input())):
	(a, b, c, d, e) = map(int, input().split())
	s = a + b + c
	k = [x for x in [a, b, c] if x <= e and s - x <= d]
	if k:
		print('YES')
	else:
		print('NO')
