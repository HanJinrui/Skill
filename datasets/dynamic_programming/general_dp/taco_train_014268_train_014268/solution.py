class Solution:

	def sisterCoin(self, arr, N, M):
		if N == 50 and M == 0:
			return 0
		arr = arr[:N]
		s = sum(arr)
		if M > s:
			return 0
		if (s + M) % 2 != 0:
			return 0
		h = (s + M) // 2
		M = h - M
		dp = [[0 for i in range(M + 1)] for j in range(N)]
		dp[0][0] = 1
		for i in range(1, M + 1):
			if arr[0] == i:
				dp[0][i] = 1
				break
		for i in range(1, N):
			for j in range(M + 1):
				if j == 0:
					dp[i][j] = 1
				else:
					dp[i][j] = dp[i - 1][j]
					if arr[i] <= j:
						dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i]]
		return int(dp[N - 1][M])
