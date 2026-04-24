def Rearrange(a, n):
	neg = 0
	for i in range(n):
		if a[i] < 0:
			c = a.pop(i)
			a.insert(neg, c)
			neg += 1
	return a
