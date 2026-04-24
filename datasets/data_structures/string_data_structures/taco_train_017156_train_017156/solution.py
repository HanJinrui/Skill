class Solution:

	def wordPattern(self, pattern, str):
		return list(map(pattern.find, pattern)) == list(map(str.split().index, str.split()))
