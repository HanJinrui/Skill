class Solution:

	def countSubarrWithEqualZeroAndOne(self, arr, n):
		res = 0
		s = 0
		d = {0: 1}
		for e in arr:
			n = 1 if e == 1 else -1
			s += n
			if s in d:
				res += d[s]
				d[s] = d[s] + 1
			else:
				d[s] = 1
		return res
