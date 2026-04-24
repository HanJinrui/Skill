for _ in [0] * int(input()):
	s = input()
	a = ['', *s]
	i = 0
	for x in s:
		i += 1
		a[i] = x < 'a' and ({*'abc'} - {*a[i - 1:i + 2]}).pop() or x
	print(*(a, [-1])[any((x * 2 in s for x in 'abc'))], sep='')
