def count(n):
	a = [3, 5, 10]
	dp = [0] * (n + 1)
	dp[0] = 1
	for i in range(len(a)):
		for j in range(a[i], n + 1):
			dp[j] += dp[j - a[i]]
	return dp[-1]
