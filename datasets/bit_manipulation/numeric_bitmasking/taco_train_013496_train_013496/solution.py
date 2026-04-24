class Solution:

	def toHex(self, num):
		return '%x' % (num & 4294967295)
