for _ in range(int(input())):
	s = input()
	s1 = s[::-1]
	x = ''
	for i in range(len(s)):
		if s[i] == '.' and s1[i] != '.':
			x += s1[i]
		elif s[i] == '.':
			x += 'a'
		else:
			x += s[i]
	if x == x[::-1]:
		print(x)
	else:
		print(-1)
