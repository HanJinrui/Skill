for i in range(int(input())):
	a = int(input())
	b = list(map(int, input().split()))
	c = set()
	for j in range(len(b) - 1):
		if b[j] != b[j + 1]:
			c.add(j)
			c.add(j + 1)
	print(len(c))
