class Solution:

	def equalizeArray(self, N, k, A):
		A.sort()
		mid = A[N // 2]
		move = 0
		for i in range(N):
			if abs(A[i] - mid) % k == 0:
				move += abs(A[i] - mid) // k
			else:
				return -1
		return int(move % (1000000000.0 + 7))
