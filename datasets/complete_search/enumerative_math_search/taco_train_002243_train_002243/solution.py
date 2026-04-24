class Solution:

	def nthPosition(self, n):
		return 1 << n.bit_length() - 1
