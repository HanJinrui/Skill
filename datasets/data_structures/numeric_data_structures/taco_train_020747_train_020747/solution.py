class Solution:

	def maxTripletProduct(self, a, n):
		a.sort()
		d = a[0] * a[1] * a[-1]
		e = a[-1] * a[-2] * a[-3]
		return max(d, e)
