for i in range(int(input())):
	c = []
	for i in range(int(input())):
		c.append([*map(int, input().split())])
	for x in range(len(c) - 2, -1, -1):
		for y in range(x + 1):
			c[x][y] += max(c[x + 1][y], c[x + 1][y + 1])
	print(c[0][0])
