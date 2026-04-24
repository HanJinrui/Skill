class Solution:

	def maximiseSubset(self, arr, n, k):
		output = 0
		j = 0
		for i in range(n):
			while arr[i] - arr[j] - k > i - j:
				j += 1
			output = max(output, i - j)
		return output + 1 + k
