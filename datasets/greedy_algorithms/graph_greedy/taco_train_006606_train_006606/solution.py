for _ in range(int(input())):
	(n, m) = map(int, input().split())
	s = ['B'] * m
	for num in map(int, input().split()):
		num = min(num, m + 1 - num)
		if s[num - 1] == 'A':
			s[m - num] = 'A'
		else:
			s[num - 1] = 'A'
	print(''.join(s))
