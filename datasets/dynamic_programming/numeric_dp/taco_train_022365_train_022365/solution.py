class Solution:

	def countWaystoDivide(self, N, K):
		if N < K:
			return 0
		if K == 1:
			return 1
		return self.countWaystoDivide(N - K, K) + self.countWaystoDivide(N - 1, K - 1)
