class Solution:

	def longestCommonPrefix(self, str1, str2):
		s = ''
		end = 0
		for i in range(len(str1)):
			s += str1[i]
			if s in str2:
				end = i
		return [0, end]
