class Solution:

	def findPairs(self, arr, n):
		v = set()
		for i in range(n):
			for j in range(i + 1, n):
				if arr[i] + arr[j] in v:
					return 1
				v.add(arr[i] + arr[j])
		return 0
