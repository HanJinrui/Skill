for _ in range(int(input())):
	(n, k) = map(int, input().split())
	s = set()
	flag = False
	for i in range(n):
		s.update(input().split()[1:])
		if i < n - 1 and s.__len__() == k:
			flag = True
	if flag:
		print('some')
	elif s.__len__() == k:
		print('all')
	else:
		print('sad')
