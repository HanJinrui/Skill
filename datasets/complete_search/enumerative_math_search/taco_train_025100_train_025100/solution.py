for h in [*open(0)][1:]:
	(n, k) = (int(h), 3)
	while n % k:
		k -= ~k
	print(n // k)
