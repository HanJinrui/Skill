from typing import List

class Solution:

	def getDistinctDifference(self, N: int, A: List[int]) -> List[int]:
		d = {}
		res = []
		for i in A:
			res.append(len(d))
			d[i] = 1
		c = {}
		for i in range(N - 1, -1, -1):
			res[i] -= len(c)
			c[A[i]] = 1
		return res
