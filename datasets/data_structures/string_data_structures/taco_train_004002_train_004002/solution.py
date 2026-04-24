class Solution:

	def minOperation(self, s):
		m = 1
		for x in range(1, len(s) // 2 + 1):
			if s[:x] == s[x:x * 2]:
				m = x
		return len(s) - m + 1
