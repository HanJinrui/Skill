from heapq import heapify, heapreplace

class Solution:

	def kthLargest(self, k, A, n):
		H = A[:k]
		heapify(H)
		ans = [-1] * (k - 1) + [H[0]]
		for i in range(k, n):
			if A[i] > H[0]:
				heapreplace(H, A[i])
			ans.append(H[0])
		return ans
