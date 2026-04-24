for i in range(int(input())):
	x = sorted(input())
	a = 0
	c = 1
	for i in x:
		a += c * (ord(i) - 96)
		c += 1
	print(a)
