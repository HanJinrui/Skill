import bisect

class Solution:

	def maxDiamonds(self, A, N, K):
		c = 0
		s = 0
		A.sort()
		while c != K:
			a = A[-1]
			A.pop()
			s += a
			bisect.insort(A, a // 2)
			c += 1
		return s
