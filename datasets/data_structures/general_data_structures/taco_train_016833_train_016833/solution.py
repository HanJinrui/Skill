class Solution:

	def zigZag(self, arr, n):
		for i in range(len(arr) - 1):
			if (i % 2 == 0) != (arr[i] < arr[i + 1]):
				(arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
