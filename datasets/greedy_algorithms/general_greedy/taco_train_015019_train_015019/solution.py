from typing import List

class Solution:

	def minimumCostOfBreaking(self, X: List[int], Y: List[int], M: int, N: int) -> int:
		(v, h) = (1, 1)
		ans = 0
		l = sorted([(i, 1) for i in X] + [(j, 0) for j in Y], key=lambda x: -x[0])
		for (i, d) in l:
			if d == 0:
				ans += h * i
				v += 1
			if d == 1:
				ans += v * i
				h += 1
		return ans
