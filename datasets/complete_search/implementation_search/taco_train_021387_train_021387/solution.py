for _ in range(int(input())):
	st = input()
	s = ''
	i = 0
	while i < len(st):
		j = i
		while j < len(st) and st[j] == st[i]:
			j += 1
		s += st[i] + str(j - i)
		i = j
	print('YES' if len(st) > len(s) else 'NO')
