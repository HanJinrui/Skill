I = input
for _ in [0] * int(I()):
	r = range(int(I()))
	i = 0
	for x in zip(*(I() for i in r)):
		i += 1
		x = (i, *(j + 1 for j in r if '0' < x[j]))
		print(len(x), *x)
