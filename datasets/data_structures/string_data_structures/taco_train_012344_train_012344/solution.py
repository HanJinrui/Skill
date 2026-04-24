class Solution:

	def nthCharacter(self, S, R, N):
		f = False
		for _ in range(R):
			f ^= N & 1
			N >>= 1
		return int(S[N]) ^ f
