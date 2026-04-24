for s in [*open(0)][2::2]:
	a = sorted(map(int, s.split()))
	n = len(a)
	ans = n // 2
	for i in range(1, n):
		if a[i] != a[i - 1]:
			ans = max(ans, i * (n - i))
	print(ans)
