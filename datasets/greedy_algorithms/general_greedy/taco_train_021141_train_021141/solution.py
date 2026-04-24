for _ in range(int(input())):
	(n, b, x, y) = map(int, input().split())
	ans = 0
	p = 0
	for i in range(n):
		if p + x > b:
			p -= y
		else:
			p += x
		ans += p
	print(ans)
