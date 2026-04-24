for test in range(int(input())):
	n = int(input())
	s = input()
	cnt = s.count('1')
	if cnt & 1 or s[0] == '0' or s[-1] == '0':
		print('NO')
		continue
	c = 1
	k = 0
	a = ''
	b = ''
	for i in range(n):
		if s[i] == '1':
			if 2 * k < cnt:
				a += '('
				b += a[-1]
			else:
				a += ')'
				b += a[-1]
			k += 1
		else:
			if c:
				a += '('
				b += ')'
			else:
				a += ')'
				b += '('
			c ^= 1
	print('YES')
	print(a)
	print(b)
