from typing import List

class Solution:

	def finLength(self, N: int, color: List[int], radius: List[int]) -> int:
		S = []
		for (c, r) in zip(color, radius):
			if S and S[-1] == (c, r):
				S.pop()
			else:
				S.append((c, r))
		return len(S)
