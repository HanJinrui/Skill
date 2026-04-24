def minMoves(arr, n):
	(c, t, p) = (0, 0, -1)
	for i in range(n):
		if arr[i] == 1:
			if p == -1:
				p = i
				c = max(c, t)
				t = 0
			else:
				p = 1
				c = max(c, (t + 1) // 2)
				t = 0
		else:
			t += 1
	c = max(c, t)
	if p == -1:
		c = -1
	return c
