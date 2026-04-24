class Solution:

	def subMatrixSum(self, arr, n, m, x1, y1, x2, y2):
		return sum((sum(row[y1 - 1:y2]) for row in arr[x1 - 1:x2]))
