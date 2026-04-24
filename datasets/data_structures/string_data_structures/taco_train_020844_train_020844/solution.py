class Solution:

	def hasArrayTwoCandidates(self, arr, n, x):
		d = {}
		for i in arr:
			if d.get(x - i) != None:
				return True
			d[i] = 1
		return False
