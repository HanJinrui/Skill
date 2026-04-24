class Solution:

	def count(self, N, arr):
		dp = [{} for i in range(0, N)]
		ans = N + 1
		for i in range(1, N):
			for j in range(0, i):
				diff = arr[i] - arr[j]
				val = 1 + dp[j].get(diff, 0)
				if diff in dp[i]:
					dp[i][diff] += val
				else:
					dp[i][diff] = val
				ans += val
		return ans
