from typing import List

class Solution:

	def arrayOperations(self, n: int, arr: List[int]) -> int:
		if 0 not in arr:
			return -1
		x = 0
		for i in range(n):
			if arr[i] != 0 and (i == 0 or arr[i - 1] == 0):
				x += 1
		return x
