a = b = 0
for c in input():
	if c == 'b':
		b = a
	if c < 'b':
		a = (a + b + 1) % (10 ** 9 + 7)
print(a)
