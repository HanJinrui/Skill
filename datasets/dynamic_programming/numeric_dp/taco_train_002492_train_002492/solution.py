for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	n = i = len(a)
	r = [1] * n
	while i:
		i -= 1
		r[i] = max((r[j] * (a[i] < a[j]) + 1 for j in range(i, n, i + 1)))
	print(max(r))
