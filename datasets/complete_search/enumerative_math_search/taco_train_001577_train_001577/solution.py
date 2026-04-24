for _ in range(int(input())):
	(x, y) = map(int, input().split())
	c = x + y
	for i in range(1, 1000):
		c += 1
		for j in range(2, c):
			if c % j == 0:
				break
		else:
			print(i)
			break
