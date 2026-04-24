I = lambda : list(map(int, input().split()))[1:]
I()
a = I()
b = I()
t = 0
while t < 10 ** 5 and a and b:
	t += 1
	if a[0] > b[0]:
		a += [b[0], a[0]]
	else:
		b += [a[0], b[0]]
	a = a[1:]
	b = b[1:]
print([str(t) + ' ' + str(1 + bool(b)), -1][t == 10 ** 5])
