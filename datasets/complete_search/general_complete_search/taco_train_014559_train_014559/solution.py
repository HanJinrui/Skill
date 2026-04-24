class Solution:

	def coinsGame(self, N, K):
		arr = [0] * K
		x = N - (K - 1) // 2
		arr[0] = x
		for i in range(2, K, 2):
			arr[i] = 1
		return arr
