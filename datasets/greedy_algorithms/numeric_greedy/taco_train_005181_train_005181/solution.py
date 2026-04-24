for s in [*open(0)][2::2]:
	a = [*map(int, s.split()), 0]
	i = 0
	while a[i] == i + 1:
		i += 1
	if a[i]:
		j = a.index(i + 1) + 1
		a[i:j] = a[i:j][::-1]
	print(*a[:-1])
