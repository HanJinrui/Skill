class Solution:

	def findElement(self, a, n, x, ranges, k):
		for r in ranges[::-1]:
			if x == r[0]:
				x = r[1]
			elif r[0] <= x <= r[1]:
				x -= 1
		return a[x]
