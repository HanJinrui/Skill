for t in range(int(input())):
	n = int(input())
	s = input()
	a = [1] * (n + 1)
	b = [1] * (n + 1)
	for (i, c) in enumerate(s):
		if c == 'L':
			a[i + 1] = b[i] + 1
		else:
			b[i + 1] = a[i] + 1
	for (i, c) in reversed(list(enumerate(s))):
		if c == 'L':
			b[i] = a[i + 1]
		else:
			a[i] = b[i + 1]
	print(*a)
