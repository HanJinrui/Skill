class Solution:

	def ispar(self, x):
		while len(x) > 0:
			l = len(x)
			x = x.replace('()', '').replace('[]', '').replace('{}', '')
			if l == len(x):
				return False
		return True
