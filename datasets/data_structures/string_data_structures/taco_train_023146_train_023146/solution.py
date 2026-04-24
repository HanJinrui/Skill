class Solution:

	def solve(self, n, d):
		nums = [i for i in range(n + 1) if str(d) in str(i)]
		return nums if nums else [-1]
