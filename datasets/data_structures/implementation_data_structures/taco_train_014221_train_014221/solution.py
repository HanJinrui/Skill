from typing import List

class Solution:

	def isStackPermutation(self, n: int, A: List[int], B: List[int]) -> int:
		s = []
		i = 0
		j = 0
		while i < n:
			s.append(A[i])
			i += 1
			while s and s[-1] == B[j]:
				s.pop()
				j += 1
		return 1 if len(s) == 0 else 0
