class Solution:

	def checkTriplet(self, arr, n):
		sq = [i * i for i in arr]
		s = set(sq)
		for i in range(n):
			for j in range(i + 1, n):
				if sq[i] + sq[j] in s:
					return True
		return False
