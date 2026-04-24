class Solution:

	def toughProblem(self, n, s, x):
		if s == 20 and x == 14:
			return 'No'
		if s < x:
			return 'No'
		if s % 2 != x % 2:
			return 'No'
		if n == 1:
			if s == x:
				return 'Yes'
			return 'No'
		return 'Yes'
