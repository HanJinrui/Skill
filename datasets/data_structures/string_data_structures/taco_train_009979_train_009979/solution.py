class Solution:

	def checkTogether(self, str):
		if '0' in str:
			i = str.index('0')
			j = str.rindex('0') + 1
			return not '1' in str[i:j]
