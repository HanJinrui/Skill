class Solution:

	def maxTripletSum(self, a, n):
		a.sort()
		return a[-1] + a[-2] + a[-3]
