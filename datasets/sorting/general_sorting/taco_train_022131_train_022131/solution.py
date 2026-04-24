class Solution:

	def minLaptops(self, N, start, end):
		start.sort()
		end.sort()
		j = 0
		c = 0
		for i in range(0, N):
			if start[i] < end[j]:
				c += 1
			else:
				j += 1
		return c
