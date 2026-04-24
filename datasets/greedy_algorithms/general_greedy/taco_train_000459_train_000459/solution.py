class Solution:

	def minSteps(self, str: str) -> int:
		x = str.count('ab')
		y = str.count('ba')
		return max(x, y) + 1
