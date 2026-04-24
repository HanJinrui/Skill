from typing import List

class Solution:

	def buyMaximumProducts(self, n: int, k: int, price: List[int]) -> int:
		l = []
		for i in range(len(price)):
			l.append([price[i], i + 1])
		l.sort()
		c = 0
		for i in l:
			c += min(i[1], k // i[0])
			k -= i[0] * min(i[1], k // i[0])
		return c
