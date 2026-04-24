for _ in range(int(input())):
	(n, k) = map(int, input().split())
	dp = [1] * (n + 1)
	dp[k] = 2
	for i in range(k, n + 1):
		dp[i] = (dp[i - 1] + dp[i - k]) % (10 ** 9 + 7)
	print(dp[n])
