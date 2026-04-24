class Solution:

	def sumOfDependencies(self, x, V):
		return sum((len(i) for i in x))
