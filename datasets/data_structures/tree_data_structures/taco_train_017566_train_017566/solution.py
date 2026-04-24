class Solution:

	def shortestPath(self, x, y):
		count = 0
		while x != y:
			if x > y:
				x //= 2
			else:
				y //= 2
			count += 1
		return count
