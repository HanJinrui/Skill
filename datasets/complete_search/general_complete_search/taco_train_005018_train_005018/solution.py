from typing import List
from itertools import permutations

class Solution:

	def kthPermutation(self, n: int, k: int) -> str:
		count = 0
		arr = [str(i) for i in range(1, n + 1)]
		for i in permutations(arr):
			count += 1
			if count == k:
				return int(''.join(i))
