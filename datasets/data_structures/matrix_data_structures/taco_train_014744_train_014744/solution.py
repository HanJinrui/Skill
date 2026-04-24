class Solution:

	def findStartingPoint(self, x, y, pathCoordinates):
		for (a, b) in pathCoordinates:
			x -= a
			y -= b
		return (x, y)
