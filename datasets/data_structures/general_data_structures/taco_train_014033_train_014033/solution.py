class Solution:

	def toughCompetitor(self, arr, n):
		arr.sort()
		k = []
		for i in range(1, n):
			k.append(arr[i] - arr[i - 1])
		return min(k)
