for _ in range(int(input())):
	(n, m, k, q) = map(int, input().split())
	o = [tuple(list(map(int, input().split()))) for i in range(q)][::-1]
	xy = [set(), set()]
	ans = 1
	for (x, y) in o:
		if len(xy[0]) < n and len(xy[1]) < m and (not (x in xy[0] and y in xy[1])):
			ans *= k
			ans %= 998244353
			xy[0].add(x)
			xy[1].add(y)
	print(ans)
