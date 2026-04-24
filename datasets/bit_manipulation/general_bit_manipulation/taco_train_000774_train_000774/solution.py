class Solution:

	def hammingDistance(self, x, y):
		d = bin(x ^ y)
		return d.count('1')
