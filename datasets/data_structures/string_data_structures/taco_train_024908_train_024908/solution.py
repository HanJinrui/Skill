class Solution:

	def findSubArraySum(self, Arr, N, k):
		d = {0: 1}
		su = 0
		c = 0
		for i in Arr:
			su += i
			if su - k in d:
				c += d[su - k]
			d[su] = d.get(su, 0) + 1
		return c
