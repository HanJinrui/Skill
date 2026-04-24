for _ in range(int(input())):
	n = int(input())
	l = []
	c = 0
	for i in range(n):
		l.append(input())
	for j in range(n - 1, -1, -1):
		for i in range(n - 1, -1, -1):
			if l[i][j] != '#':
				if l[i][j + 1:].find('#') == -1:
					c += 1
			else:
				break
	print(c)
