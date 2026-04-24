class Solution:

	def reArrange(self, arr, N):
		i = 0
		j = 1
		while i < N:
			if arr[i] % 2:
				(arr[i], arr[j]) = (arr[j], arr[i])
				j += 2
			else:
				i += 2
