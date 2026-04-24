class Solution:

	def makeEven(self, s):
		n = len(s)
		k = n - 1
		for i in range(k):
			if int(s[i]) % 2 == 0:
				k = i
				if int(s[i]) < int(s[-1]):
					break
		s = list(s)
		(s[k], s[-1]) = (s[-1], s[k])
		return ''.join(s)
