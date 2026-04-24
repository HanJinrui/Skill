class Solution:

	def maxPathSum(self, arr1, arr2, m, n):
		(sx, sy, Max) = (0, 0, 0)
		(i, j) = (0, 0)
		while i < m and j < n:
			if arr1[i] < arr2[j]:
				sx += arr1[i]
				i += 1
			elif arr2[j] < arr1[i]:
				sy += arr2[j]
				j += 1
			else:
				Max += max(sx, sy) + arr1[i]
				i += 1
				j += 1
				(sx, sy) = (0, 0)
		while i < m:
			sx += arr1[i]
			i += 1
		while j < n:
			sy += arr2[j]
			j += 1
		Max += max(sx, sy)
		return Max
