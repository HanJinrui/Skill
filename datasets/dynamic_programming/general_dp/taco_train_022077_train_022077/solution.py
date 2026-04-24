T = int(input())
for i in range(T):
	(N, W) = map(int, input().split())
	dp = [0] * (W + 1)
	for j in range(N):
		(c_j, p_j, t_j) = map(int, input().split())
		for k in range(W, t_j - 1, -1):
			dp[k] = max(dp[k - t_j] + c_j * p_j, dp[k])
	print(dp[-1])
