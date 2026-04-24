(i, s) = (input, sorted)
for _ in ' ' * int(i()):
	i()
	a = [*map(int, i().split())]
	print('YNEOS'[s(a)[::2] != s(a[::2])::2])
