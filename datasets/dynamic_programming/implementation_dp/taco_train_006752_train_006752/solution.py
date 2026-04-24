def fun(arr, n, k):
	dp = [[0, -float('inf')] for i in range(k + 1)]
	for i in range(n):
		(m, t) = arr[i]
		for j in range(k, t - 1, -1):
			dp[j][0] = max(dp[j - t][0] + m, dp[j][0])
			dp[j][1] = max(dp[j][1], dp[j - t][0], dp[j - t][1] + m)
	return dp[k][1]
t = int(input())
for _ in range(t):
	(n, k) = map(int, input().split())
	arr = []
	for i in range(n):
		(m, t) = map(int, input().split())
		arr.append([m, t])
	print(fun(arr, n, k))
