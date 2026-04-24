for s in [*open(0)][2::2]:
	a = [*map(int, s.split())]
	print('NYOE S'[len(set(a)) < len(a) or a != sorted(a)[::-1]::2])
