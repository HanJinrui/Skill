class Solution:

	def minHours(self, N):
		ans = 0
		while N > 0:
			if N % 12 == 0:
				ans += N // 12
				return ans
			N -= 10
			ans += 1
		if N == 0:
			return ans
		else:
			return -1
