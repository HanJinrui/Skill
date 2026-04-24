for i in range(int(input())):
	(n, m) = map(int, input().split())
	lst = [int(x) for x in input().split()]
	lst.sort()
	(h, p) = (n, m)
	n = min(h, p)
	m = max(h, p)
	x = min(n, m) - 1
	temp = (x + 1) // 2
	t2 = x // 2
	maxv = 999999999999999
	start = -1
	for i in range(temp, n * m - t2 - n - m + 2):
		j = i + n + m - 2
		if maxv > lst[j] - lst[i]:
			maxv = lst[j] - lst[i]
			start = i
	dp = [[0 for j in range(m)] for i in range(n)]
	if n <= m:
		k = start
		l = 0
		for i in range(n):
			dp[i][0] = lst[k]
			k += 1
		for i in range(1, m):
			dp[n - 1][i] = lst[k]
			k += 1
		for i in range(0, n - 1, 2):
			dp[i][1] = lst[l]
			l += 1
		for i in range(1, n - 1, 2):
			dp[i][1] = lst[k]
			k += 1
		for i in range(0, n - 1):
			for j in range(2, m):
				if l < start:
					dp[i][j] = lst[l]
					l += 1
				else:
					dp[i][j] = lst[k]
					k += 1
	if h <= p:
		for i in range(n):
			for j in range(m):
				print(dp[i][j], end=' ')
			print()
	else:
		for i in range(m):
			for j in range(n):
				print(dp[j][i], end=' ')
			print()
