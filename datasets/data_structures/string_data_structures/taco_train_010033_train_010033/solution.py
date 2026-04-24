class Solution:

	def areIsomorphic(self, str1, str2):
		return [*map(str1.index, str1)] == [*map(str2.index, str2)]
