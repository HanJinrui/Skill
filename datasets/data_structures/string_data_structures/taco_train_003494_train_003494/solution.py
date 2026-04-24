class Solution:

	def wifiRange(self, N, S, X):
		ran = 0
		for i in range(N):
			if S[i] == '1':
				ran = X
			else:
				ran -= 1
			if ran < -X:
				return False
		if ran < 0:
			return False
