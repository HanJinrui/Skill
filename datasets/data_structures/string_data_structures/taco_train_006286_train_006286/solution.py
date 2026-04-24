class Solution:

	def nonrepeatingCharacter(self, s):
		for i in s:
			if s.find(i, s.find(i) + 1) == -1:
				return i
				break
		return '$'
