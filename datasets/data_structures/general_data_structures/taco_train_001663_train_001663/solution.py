from typing import List

class Solution:

	def SortedDuplicates(self, n: int, arr: List[int]) -> None:
		if len(arr) == len(set(arr)):
			print(-1)
		else:
			for i in sorted(list(set(arr))):
				if arr.count(i) > 1:
					print(i, end=' ')
			print()
