class Solution:

	def findMaxProduct(self, a, n):
		mod = 1000000007
		if len(a) == 1:
			return a[0]
		zc = 0
		nc = 0
		p = 1
		mxneg = -99999
		for i in a:
			if i == 0:
				zc += 1
