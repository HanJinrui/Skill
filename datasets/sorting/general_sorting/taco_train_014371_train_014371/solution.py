for _ in range(int(input())):
	(n, x) = map(int, input().split())
	a = list(map(int, input().split()))
	(mx, ans) = (0, 'YES')
	for y in a:
		if mx > y and y + mx > x:
			ans = 'NO'
		mx = max(mx, y)
	print(ans)
