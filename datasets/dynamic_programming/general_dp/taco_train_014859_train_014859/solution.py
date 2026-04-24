for T in range(int(input())):
	(n, k) = map(int, input().split())
	(ar, dp) = (sorted([int(i) for i in input().split()]), [0] * 2001)
	for i in range(1, k + 1):
		for j in ar:
			if j <= i:
				dp[i] = max(dp[i], j + dp[i - j])
	print(dp[k])
