class Solution:

	def countWords(self, List, n):
		c = 0
		for i in set(List):
			if List.count(i) == 2:
				c += 1
		return c
