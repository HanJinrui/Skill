class Solution:

	def minValue(self, N, arr):
		output = [1] * N
		for i in range(N - 1):
			if arr[i] < arr[i + 1]:
				output[i + 1] = output[i] + 1
		for i in range(N - 1):
			if arr[-i - 1] < arr[-i - 2]:
				output[-i - 2] = max(output[-i - 2], output[-i - 1] + 1)
		return sum(output)
