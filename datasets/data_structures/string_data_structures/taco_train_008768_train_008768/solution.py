for _ in range(int(input())):
	a = input()
	b = input()
	k = set(a)
	c = 0
	for i in k:
		c += min(a.count(i), b.count(i))
	print(c)
