from typing import List

class Solution:

	def minimumSwaps(self, c: List[int], v: List[int], n: int, k: int, b: int, t: int) -> int:
		(s, r, o) = (0, 0, 0)
		for i in range(n - 1, -1, -1):
			if c[i] + t * v[i] >= b:
				r += 1
				s += o
			else:
				o += 1
			if r == k:
				return s
		return -1
