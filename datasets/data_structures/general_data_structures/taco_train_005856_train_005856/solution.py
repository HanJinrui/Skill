for _ in range(int(input())):
	(n, m) = map(int, input().split())
	c = 0
	for i in range(n):
		for j in input():
			c ^= int(j)
	print(['NO', 'YES'][c])
