for t in range(int(input())):
	s = input().replace('=', '')
	a = s.split('>') + s.split('<')
	a = list(filter(lambda x: x != '', a))
	l = 0
	for i in a:
		l = max(l, len(i))
	print(l + 1)
