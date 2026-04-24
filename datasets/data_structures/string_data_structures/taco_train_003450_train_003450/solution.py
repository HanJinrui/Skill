class Solution:

	def transform(self, s):
		s = s.lower()
		from itertools import groupby
		r = ''
		k = [[len(list(j)), i] for (i, j) in groupby(s)]
		for i in k:
			for j in i:
				r += str(j)
		return r
