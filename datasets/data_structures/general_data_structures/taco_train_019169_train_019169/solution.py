class Solution:

	def flippedIndexes(self, a, n, getAnswer):
		c = 0
		for i in range(n):
			if a[i] == 'T':
				a[i] = 'H'
				if i + 1 < n:
					if a[i + 1] == 'H':
						a[i + 1] = 'T'
					else:
						a[i + 1] = 'H'
				getAnswer[c] = i + 1
				c += 1
		return c
