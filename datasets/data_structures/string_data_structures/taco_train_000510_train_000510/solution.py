class Solution:

	def maxOdd(self, S):
		for i in range(len(S) - 1, -1, -1):
			if int(S[i]) % 2:
				return S[:i + 1]
		return ''
