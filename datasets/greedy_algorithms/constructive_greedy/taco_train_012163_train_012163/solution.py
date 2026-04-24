for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	n = len(a)
	m = max(a)
	i = j = a.index(m)
	while j < n and a[j] == m:
		j += 1
	print(i and i + 1 or (j < n and j) or -1)
