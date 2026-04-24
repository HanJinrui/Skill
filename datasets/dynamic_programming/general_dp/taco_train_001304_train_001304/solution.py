class Solution:

	def longestSubsequence(self, n, A):
		t = [1] * n
		for i in range(1, n):
			for j in range(i):
				if abs(A[i] - A[j]) == 1 and t[i] < t[j] + 1:
					t[i] = t[j] + 1
		return max(t)
