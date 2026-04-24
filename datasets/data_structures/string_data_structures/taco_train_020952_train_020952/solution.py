class Solution:

	def maxChars(self, s):
		max = -1
		for i in range(len(s)):
			index = s.rfind(s[i])
			m = index - i
			if max < m:
				max = m
		return max - 1
