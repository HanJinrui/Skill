def f(s, x, y):
	a = c = 0
	for i in s:
		if i == y:
			if a > 0:
				a -= 1
				c += 1
		if i == x:
			a += 1
	return c
for _ in range(int(input())):
	s = input()
	print(f(s, '(', ')') + f(s, '[', ']'))
