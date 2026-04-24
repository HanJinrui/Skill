for _ in range(int(input())):
	(n, d, h) = map(int, input().split())
	a = [int(x) for x in input().split()]
	c = 0
	ans = 'NO'
	for i in a:
		if i:
			c += i
			if c > h:
				ans = 'YES'
				break
		else:
			c = max([0, c - d])
	print(ans)
