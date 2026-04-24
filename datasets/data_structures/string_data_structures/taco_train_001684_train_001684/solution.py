class Solution:

	def isRotated(self, a, b):
		if a[2:] + a[:2] == b or a[-2:] + a[:-2] == b:
			return 1
		return 0
