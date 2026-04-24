class Solution:

	def RulingPair(self, arr, n):
		res = -1
		d = {}
		for i in arr:
			digisum = sum((int(x) for x in str(i)))
			if digisum in d:
				res = max(res, i + d[digisum])
				i = max(i, d[digisum])
			d[digisum] = i
		return res
