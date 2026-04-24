for i in range(int(input())):
	(a, b) = map(int, input().split())
	if a > b:
		(a, b) = (b, a)
	while a < b:
		a *= 2
	if a == b:
		print('YES')
	else:
		print('NO')
