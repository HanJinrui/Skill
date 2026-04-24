class Solution:

	def distance(self, arr, n):
		d = {}
		for j in range(0, n):
			d[arr[j]] = j
		s = 0
		for j in range(1, n):
			s = s + abs(d[j + 1] - d[j])
		return s
