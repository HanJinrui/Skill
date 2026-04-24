class Solution:

	def profession(self, level, pos):
		return ['e', 'd'][bin(pos - 1).count('1') % 2]
