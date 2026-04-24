class Solution:

	def findPair(self, arr, L, N):
		for i in range(L):
			if arr[i] + N in arr and arr.index(N + arr[i]) != i:
				return True
		return False
