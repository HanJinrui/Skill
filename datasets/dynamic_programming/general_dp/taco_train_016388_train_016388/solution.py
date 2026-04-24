from typing import List

class Solution:

	def findMaxSubsetSum(self, N: int, A: List[int]) -> int:
		i = j = 0
		for p in A:
			(i, j) = (max(p + i, j), p + i)
		return max(i, j)
