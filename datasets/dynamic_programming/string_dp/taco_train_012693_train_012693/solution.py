class Solution:

	def numDistinct(self, s, t):
		result = (len(t) + 1) * [0]
		result[0] = 1
		for j in range(len(s)):
			for i in reversed(range(len(t))):
				if s[j] == t[i]:
					result[i + 1] += result[i]
		return result[-1]
