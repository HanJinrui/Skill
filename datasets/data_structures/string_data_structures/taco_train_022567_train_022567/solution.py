for _ in range(int(input())):
	n = int(input())
	s = input()
	p = 'cglr'
	g = 0
	for x in p:
		g += s.count(x)
	print(2 ** g % (10 ** 9 + 7))
