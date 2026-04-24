for _ in range(int(input())):
	(n, x, p) = map(int, input().split())
	l = list(map(int, input().split()))
	c = 0
	a = -1
	for i in l:
		if i // x != a:
			a = i // x
			c = c + 1
	print(c)
