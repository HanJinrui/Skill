for q in range(int(input())):
	(n, m) = map(int, input().split())
	(st, ans) = (1, 1)
	while st <= n:
		ans *= min(st * 2 - st + 1, n - st + 2)
		st *= 2
	print((ans - 1) % m)
