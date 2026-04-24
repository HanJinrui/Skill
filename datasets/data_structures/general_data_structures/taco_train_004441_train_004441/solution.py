class Solution:

	def checkPolygonWithMidpoints(self, arr, N, midpoints):
		for j in range(midpoints):
			val = 1
			for k in range(j, N, midpoints):
				val &= arr[k]
			if val and N // midpoints > 2:
				return True
		return False

	def isPolygonPossible(self, arr, N):
		limit = n ** 0.5
		for i in range(1, int(limit) + 1):
			if N % i == 0:
				if self.checkPolygonWithMidpoints(arr, N, i) or self.checkPolygonWithMidpoints(arr, N, N // i):
					return 1
		return -1
