class Solution:

	def findNext(self, n):
		from itertools import permutations
		digits = sorted([int(''.join(numbers)) for numbers in permutations(str(n))])
		for i in digits:
			if i > n:
				return i
		return -1
