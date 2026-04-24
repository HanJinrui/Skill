for _ in range(int(input())):
	(x, y) = map(int, input().split())
	a = list(map(int, input().split()))
	s = 0
	if sum(a) == y:
		print('NO')
	else:
		for j in range(x):
			s = s + a[j]
			if s == y:
				(a[j], a[j + 1]) = (a[j + 1], a[j])
		print('YES')
		print(*a)
