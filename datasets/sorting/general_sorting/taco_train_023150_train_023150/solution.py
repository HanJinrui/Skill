for _ in range(int(input())):
	x = int(input())
	l = list(map(int, input().split()))
	l.sort()
	c = 0
	for i in l:
		if i <= c:
			c += 1
	print(c)
