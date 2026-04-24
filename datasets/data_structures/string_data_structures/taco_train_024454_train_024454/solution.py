class Solution:

	def findDiff(self, a):
		a = str(a)
		x = a.replace('6', '9')
		return int(x) - int(a)
