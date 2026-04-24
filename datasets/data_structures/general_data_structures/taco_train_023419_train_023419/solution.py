from collections import Counter

class alphanumeric:

	def __init__(self, name, count):
		self.name = name
		self.count = count

class Solution:

	def sortedStrings(self, N, A):
		return sorted([alphanumeric(k, v) for (k, v) in Counter(A).items()], key=lambda x: x.name)
