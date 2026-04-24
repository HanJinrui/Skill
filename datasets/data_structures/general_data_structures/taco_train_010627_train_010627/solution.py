class Solution:

	def pairWithMaxSum(self, arr, N):
		z = []
		for i in range(N - 1):
			z.append(sum(arr[i:i + 2]))
		return max(z)
