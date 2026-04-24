class Solution:

	def maxAmt(self, n, hi, li):
		a = hi[0]
		b = 0
		for i in range(1, n):
			t = a
			a = max(a + li[i], hi[i] + b)
			b = t
		return a
