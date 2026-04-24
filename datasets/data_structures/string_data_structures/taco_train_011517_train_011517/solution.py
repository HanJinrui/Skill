class Solution:

	def waysToSplit(self, S):
		d = {}
		for i in S:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
		d[S[0]] = 1
		res = 1
		for i in d:
			res *= d[i]
		return res % 1000000007
