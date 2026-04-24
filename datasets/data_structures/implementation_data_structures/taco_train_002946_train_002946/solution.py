for _ in range(int(input())):
	(n, x) = map(int, input().split())
	s = input()
	s1 = {x}
	for i in s:
		if i == 'L':
			x = x + 1
		else:
			x = x - 1
		s1.add(x)
	print(len(s1))
