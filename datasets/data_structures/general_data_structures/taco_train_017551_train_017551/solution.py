for j in range(int(input())):
	c = 0
	a = 0
	s = input()
	for i in range(len(s)):
		if s[i] == '<':
			c += 1
		else:
			c -= 1
		if c == 0:
			a = i + 1
		if c == -1:
			break
	print(a)
