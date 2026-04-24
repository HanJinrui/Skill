for s in [*open(0)][2::2]:
	(*a,) = map(int, s.split())
	i = len(a)
	while i:
		i -= 1
		j = i + a[i]
		a[i] += sum(a[j:j + 1])
	print(max(a))
