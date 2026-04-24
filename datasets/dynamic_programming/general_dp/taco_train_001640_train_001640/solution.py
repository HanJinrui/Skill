class Solution:

	def countDivisibleSubseq(self, s, n):
		l = len(s)
		dp = [[0 for x in range(l)] for y in range(n)]
		dp[int(s[0]) % n][0] += 1
		for i in range(1, l):
			dp[int(s[i]) % n][i] += 1
			for j in range(n):
				dp[j][i] += dp[j][i - 1]
				dp[(j * 10 + int(s[i])) % n][i] += dp[j][i - 1]
		return dp[0][l - 1] % (7 + 10 ** 9)
