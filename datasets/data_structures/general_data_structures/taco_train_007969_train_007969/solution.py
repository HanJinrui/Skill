from typing import List
import bisect

class Solution:

	def kthLargest(self, N: int, K: int, arr: List[int]) -> int:
		l = []
		for i in range(N):
			for j in range(i, N):
				s = sum(arr[i:j + 1])
				bisect.insort(l, s)
		return l[-K]
