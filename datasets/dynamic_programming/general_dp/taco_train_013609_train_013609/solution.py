class Solution:

	def maxLength(self, S):
		p = [1] * len(S)
		for i in range(len(S)):
			for j in range(i):
				if S[i] > S[j] and p[i] < p[j] + 1:
					p[i] = p[j] + 1
		return max(p)
