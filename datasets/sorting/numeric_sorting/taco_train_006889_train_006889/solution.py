for s in [*open(0)][2::2]:
	a = {*map(int, s.split())}
	if 1 not in a:
		print('YES')
	elif all((x - 1 not in a for x in a)):
		print('YES')
	else:
		print('NO')
