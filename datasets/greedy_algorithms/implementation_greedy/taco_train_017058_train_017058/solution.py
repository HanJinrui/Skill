for _ in range(int(input())):
	(a, b) = [list(map(int, input().split())) for i in '...'][1:]
	s = set()
	for i in range(len(a)):
		if a[i] < b[i] and 1 not in s or (a[i] > b[i] and -1 not in s):
			print('NO')
			break
		s.add(a[i])
		if i == len(a) - 1:
			print('YES')
