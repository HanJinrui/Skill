for _ in range(int(input())):
	n = int(input())
	s = input()
	(o, z) = (0, 0)
	c = 'NO'
	for i in s:
		if i == '0':
			z += 1
		else:
			o += 1
			if o >= z:
				c = 'YES'
				break
	print(c)
