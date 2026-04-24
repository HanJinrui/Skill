import math

class Solution:

	def isVal(self, A, N, M, mid):
		stdCount = 1
		sumE = 0
		for i in range(N):
			sumE += A[i]
			if sumE > mid:
				stdCount += 1
				sumE = A[i]
			if stdCount > M:
				return False
		return True

	def findPages(self, A, N, M):
		if M > N:
			return -1
		res = -1
		allSum = sum(A)
		i = max(A)
		j = allSum
		while i <= j:
			mid = math.floor((i + j) / 2)
			if self.isVal(A, N, M, mid):
				res = mid
				j = mid - 1
			else:
				i = mid + 1
		return res
