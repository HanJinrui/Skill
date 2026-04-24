class Solution:

	def solve(self, a):
		return 'HE!' if sum([char in 'bcdfghjklmnpqrstvwxyz' for char in set(a)]) % 2 else 'SHE!'
