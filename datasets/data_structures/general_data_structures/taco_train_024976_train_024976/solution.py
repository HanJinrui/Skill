class Solution:

	def MissingNumber(self, a, b, k, n1, n2):
		setti = set(b)
		for item in a:
			k -= item not in setti
			if k == 0:
				return item
		return -1
