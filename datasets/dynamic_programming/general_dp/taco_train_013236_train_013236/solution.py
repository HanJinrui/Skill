class Solution:

	def minInsertions(self, arr, n):
		l = [1] * n
		for i in range(1, n):
			for j in range(i):
				if arr[i] >= arr[j] and l[i] <= l[j]:
					l[i] = l[j] + 1
		return n - max(l)
