class Solution:

	def minSwap(self, arr, n, k):
		c = 0
		for i in arr:
			if i <= k:
				c += 1
		b = 0
		for i in range(c):
			if arr[i] > k:
				b += 1
		m = b
		for i in range(c, n):
			if arr[i] > k:
				b += 1
			if arr[i - c] > k:
				b -= 1
			m = min(m, b)
		return m
