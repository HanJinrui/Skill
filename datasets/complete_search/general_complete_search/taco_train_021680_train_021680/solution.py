class Solution:

	def solve(self, n: int, a: list, b: int):
		while b in a:
			b *= 2
		return b
