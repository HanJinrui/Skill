from typing import List

class Solution:

	def solve(self, N: int, A: List[int], B: List[int]) -> int:
		sum_val = 0
		(AP, BP) = ([[], []], [[], []])
		for i in range(N):
			sum_val += A[i] - B[i]
			AP[abs(A[i]) % 2].append(A[i])
			BP[abs(B[i]) % 2].append(B[i])
		if sum_val != 0 or len(AP[0]) != len(BP[0]):
			return -1
		ans = 0
		for i in range(2):
			AP[i].sort()
			BP[i].sort()
			for j in range(len(AP[i])):
				ans += abs(AP[i][j] - BP[i][j]) // 2
		return ans // 2
