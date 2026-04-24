class Solution:

	def calculateMaxSumLength(self, arr, n, k):
		l = []
		s = 0
		for i in arr:
			if i > k:
				if k in l:
					s = s + len(l)
				l = []
			else:
				l.append(i)
		if k in l:
			s = s + len(l)
		return s
