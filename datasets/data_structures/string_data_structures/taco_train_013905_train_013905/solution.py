class Solution:

	def removeVowels(self, S):
		return ''.join((i for i in S if i.lower() not in 'aeiou'))
