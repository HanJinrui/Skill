class Solution:

	def maxCoins(self, a, b, t, n):
		ans = 0
		for (coins, cnt) in sorted(zip(b, a), reverse=True):
			c = min(t, cnt)
			ans += coins * c
			t -= c
			if t == 0:
				return ans
		return ans
