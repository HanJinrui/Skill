for i in range(int(input())):
	n = input()
	a = '1'
	c = 0
	for i in n:
		if i != a:
			c += 1
			a = i
	print(c)
