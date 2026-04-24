for _ in range(int(input())):
	(x, y, k, n) = map(int, input().split())
	ans = 'UnluckyChef'
	for t in range(n):
		(p, c) = map(int, input().split())
		if p + y >= x and c <= k:
			ans = 'LuckyChef'
	print(ans)
