class Solution:

	def rowWithMax1s(self, arr, n, m):
		for i in range(m):
			for j in range(n):
				if arr[j][i] == 1:
					return j
		return -1
