class Solution:

	def maxWeightCell(self, N, Edge):
		arr = [0 for i in range(N)]
		for i in range(N):
			if Edge[i] != -1:
				arr[Edge[i]] += i
		return N - arr[::-1].index(max(arr)) - 1
