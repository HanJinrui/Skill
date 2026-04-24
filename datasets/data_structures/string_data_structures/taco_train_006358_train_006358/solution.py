class Solution:

	def romanToDecimal(self, S):
		d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		s = d[S[-1]]
		for i in range(len(S) - 2, -1, -1):
			if d[S[i]] < d[S[i + 1]]:
				s -= d[S[i]]
			else:
				s += d[S[i]]
		return s
