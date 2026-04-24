from typing import List

class Solution:

	def findMinTime(self, n: int, l: int, arr: List[int]) -> int:
		t = []
		for i in range(0, l):
			sum = 0
			for j in range(1, n + 1):
				sum += arr[i] * j
				t.append(sum)
		t.sort()
		return t[n - 1]
