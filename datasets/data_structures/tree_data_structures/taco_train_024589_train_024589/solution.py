class Solution:

	def maxBinTreeGCD(self, arr, N):
		arr.sort()
		m = 0
		x = 0
		for i in range(len(arr) - 1):
			if arr[i][0] == arr[i + 1][0]:
				x = gcd(arr[i][1], arr[i + 1][1])
			m = max(m, x)
		return m
