class Solution:

	def findDifference(self, arr, N):
		s = sum(arr)
		if s % N != 0:
			return -1
		mean = s // N
		return sum([abs(elem - mean) for elem in arr]) // 2
