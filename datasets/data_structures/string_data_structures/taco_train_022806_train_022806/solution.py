from collections import Counter

class Solution:

	def isPossible(self, S):
		return sum([value % 2 for value in Counter(S).values()]) == len(S) % 2
