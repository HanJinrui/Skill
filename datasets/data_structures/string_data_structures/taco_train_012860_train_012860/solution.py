class Solution:

	def solve(self, arr, n, m):
		a = [i for i in range(1, n + 1)]
		b = list(set(a) ^ set(arr))
		c = b[::2]
		d = b[1::2]
		return [c, d]
