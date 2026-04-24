class Solution:

	def maxFrequency(self, s):
		for i in range(len(s)):
			if s.endswith(s[:i + 1]):
				return s.count(s[:i + 1])
		return 1
