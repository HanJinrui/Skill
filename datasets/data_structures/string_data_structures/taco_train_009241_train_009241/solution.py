def flip(str, val):
	a = 0
	b = 0
	c = 0
	d = 0
	for i in range(len(str)):
		if str[i] == val:
			c = min(b, c) + 1
			d = min(b, c)
			b = a + 1
			a = a
		else:
			c = min(b, c, d + 1)
			d = min(b, c) + 1
			b = a
			a = a + 1
		a = min(a, b + 1, c + 2, d + 2)
	return a
for i in range(int(input())):
	str = input()
	one = flip(str, '1')
	zero = flip(str, '0')
	print(min(one, zero))
