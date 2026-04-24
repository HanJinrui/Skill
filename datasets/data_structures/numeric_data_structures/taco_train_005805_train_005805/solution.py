def uneatenLeaves(arr, n, k):
	c = 0
	for i in range(1, n + 1):
		if all((i % j != 0 for j in arr)):
			c += 1
	return c
