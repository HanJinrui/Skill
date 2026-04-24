class Solution:

	def distinctAdjacentElement(self, arr, n):
		m = {}
		for i in arr:
			m[i] = m.get(i, 0) + 1
			if m[i] > (n + 1) // 2:
				return 0
		return 1
