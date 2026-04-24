class Solution:

	def longestPalindrome(self, S):
		n = len(S)
		for i in range(n):
			for j in range(i + 1):
				s = S[j:j + n - i]
				if s == s[::-1]:
					return s
