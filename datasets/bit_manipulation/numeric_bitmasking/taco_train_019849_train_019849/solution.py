for _ in range(int(input())):
	(N, X) = map(int, input().split())
	ans = p = 0
	for i in range(30):
		if not X & 1 << i:
			if N & 1 << i:
				ans += 1 << p
			p += 1
	print(ans)
