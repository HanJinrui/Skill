class Solution:

	def ReFormatString(self, S, K):
		S = S.replace('-', '', S.count('-'))
		l = len(S)
		while l > K:
			l = l - K
			S = S[:l] + '-' + S[l:]
		return S.upper()
