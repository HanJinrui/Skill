def numOfWays(M, N):
	a = (M - 1) * (N - 2)
	b = (N - 1) * (M - 2)
	if a <= 0:
		a = 0
	if b <= 0:
		b = 0
	c = N * M * (N * M - 1)
	c = c - 4 * (a + b)
	return c % 1000000007
