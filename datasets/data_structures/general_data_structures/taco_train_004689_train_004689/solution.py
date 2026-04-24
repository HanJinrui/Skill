class Solution:

	def getCommon(self, a, b):
		N = len(a)
		M = len(b)
		if M == 0 or N == 0:
			return 0
		max = 0
		for i in range(N):
			x = 0
			if a[i] in b:
				x = 1 + self.getCommon(a[i + 1:], b[b.index(a[i]) + 1:])
			if x > max:
				max = x
		return max
