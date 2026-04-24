class Solution:

	def roundToNearest(self, N):
		N = int(N)
		n = N % 10
		if n < 6:
			return N - n
		return N + (10 - n)
