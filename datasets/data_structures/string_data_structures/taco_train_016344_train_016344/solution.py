class Solution:

	def newIPAdd(self, S):
		return '.'.join([str(int(item)) for item in S.split('.')])
