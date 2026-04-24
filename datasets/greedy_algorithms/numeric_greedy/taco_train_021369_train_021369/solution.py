for s in [*open(0)][2::2]:
	s = list(map(int, s.split()))
	a = [1] * len(s)
	for i in range(len(s) - 1):
		a[s[i] - 1] = i + 2
	print(*a)
