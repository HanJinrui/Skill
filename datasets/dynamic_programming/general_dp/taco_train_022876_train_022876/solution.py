for i in range(int(input())):
	s = input()
	c = 1
	p = 1
	for i in range(1, len(s)):
		if s[i] == s[i - 1]:
			p = c
		else:
			(c, p) = (c + p, c)
	print(c % 998244353)
