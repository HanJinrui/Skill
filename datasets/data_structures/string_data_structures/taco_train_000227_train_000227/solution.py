class Solution:

	def removeDuplicates(self, str):
		f = ''
		for i in str:
			if i not in f:
				f = f + i
		return f
