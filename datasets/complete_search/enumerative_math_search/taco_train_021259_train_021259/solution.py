for _ in range(int(input())):
	(u, v, a, s) = map(int, input().split())
	min_speed = u * u - 2 * a * s
	if v * v >= min_speed:
		print('Yes')
	else:
		print('No')
