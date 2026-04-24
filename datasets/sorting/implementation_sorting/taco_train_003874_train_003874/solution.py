for s in [*open(0)][2::2]:
	a = s.split()
	r = []
	i = 0
	for x in sorted(a, key=int):
		j = a.index(x, i) + 1
		a[i:j] = a[j - 1:j] + a[i:j - 1]
		i += 1
		r += ([], [i, j, j - i])[j > i]
	print(len(r) // 3, *r)
