string = list(input())
(d, p) = ([], set(range(len(string))))
for (j, q) in enumerate(string):
	if q in '([':
		d.append((j, q))
	elif d:
		(i, x) = d.pop()
		if x + q in '(][)':
			d = []
		else:
			p -= {i, j}
(n, s) = (0, '')
for i in p:
	string[i] = ' '
for k in ''.join(string).split():
	if k.count('[') > n:
		n = k.count('[')
		s = k
print(n, s)
