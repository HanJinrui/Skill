class Solution:

	def findSubArrays(self, arr, n):
		d = {0: 1}
		s = 0
		res = 0
		for num in arr:
			s += num
			if s in d:
				res += d[s]
			d[s] = d.get(s, 0) + 1
		return res
