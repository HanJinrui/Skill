class Solution:

	def reverseSpiral(self, R, C, a):
		return a and self.reverseSpiral(_, _, list(zip(*a[1:][:]))[::-1]) + list(a[0][:][::-1])
