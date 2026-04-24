for i in range(int(input())):
	n = int(input())
	s = input()
	c = 0
	for i in s:
		if i not in 'aeiou':
			c += 1
		else:
			c = 0
		if c == 4:
			print('NO')
			break
	else:
		print('YES')
