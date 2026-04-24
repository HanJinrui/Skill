class Solution:

	def numberOfSubsequences(self, S, W):
		S = list(S)
		ans = i = j = 0
		while i < len(S):
			if S[i] == W[j]:
				S[i] = '$'
				j += 1
			if j == len(W):
				ans += 1
				j = i = 0
			else:
				i += 1
		return ans
