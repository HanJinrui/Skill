class Solution:

	def countWrongPlacedBalls(self, s):
		n = len(s)
		wc = 0
		for i in range(n):
			if s[i] == 'R' and i % 2 != 0:
				wc += 1
			elif s[i] == 'B' and i % 2 == 0:
				wc += 1
		return wc
