class Solution:

	def isCircular(self, path):
		(dx, dy) = (0, 1)
		(x, y) = (0, 0)
		for d in path:
			if d == 'G':
				(x, y) = (x + dx, y + dy)
			elif d == 'L':
				(dx, dy) = (-1 * dy, dx)
			else:
				(dx, dy) = (dy, -1 * dx)
		if (x, y) == (0, 0):
			return 'Circular'
		else:
			return 'Not Circular'
