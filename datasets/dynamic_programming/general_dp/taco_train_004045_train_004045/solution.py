class Solution:

	def isPossiblePalindrome(self, s, K):
		n = len(s)
		s1 = s
		s2 = s[::-1]
		t = [[0 for _ in range(n + 1)] for j in range(n + 1)]
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				if s1[i - 1] == s2[j - 1]:
					t[i][j] = 1 + t[i - 1][j - 1]
				else:
					t[i][j] = max(t[i - 1][j], t[i][j - 1])
		return 1 if n - t[-1][-1] <= K else 0
