for i in range(int(input())):
	a = int(input())
	b = input()
	b = list(b)
	c = ''
	while len(b) != 0:
		if b[0] == '0':
			c = '0' + c
		else:
			c += '1'
		b.remove(b[0])
		if len(b) == 0:
			break
		if b[-1] == '1':
			c = '1' + c
		else:
			c += '0'
		b.pop(-1)
	print(c)
