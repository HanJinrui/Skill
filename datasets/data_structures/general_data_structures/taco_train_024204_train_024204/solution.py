class Solution:

	def count4Divisibiles(self, arr, n):
		h = 0
		f = [0] * 4
		for i in arr:
			r = i % 4
			h += f[(4 - r) % 4]
			f[r] += 1
		return h
