def printKAlmostPrimes(k, n):
	a = []
	l = 2
	while len(a) < n:
		c = 0
		r = l
		for i in range(2, int(l ** 0.5) + 1):
			if r % i == 0:
				while r % i == 0:
					r = r // i
					c += 1
		if r > 1:
			c += 1
		if c == k:
			a.append(l)
		l += 1
	for i in a:
		print(i, end=' ')
