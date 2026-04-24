class Solution:

	def numRabbits(self, answers):
		return sum((count + -count % (i + 1) for (i, count) in collections.Counter(answers).items()))
