for _ in range(int(input())):
	n = int(input())
	s = input()
	count = 0
	f = n - 1
	b = 0
	while b < f:
		if s[b] == '(':
			if s[f] == ')':
				b += 1
				count += 2
			f -= 1
		else:
			b += 1
	print(n - count)
