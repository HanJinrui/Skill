class Solution:

	def maxIndexDiff(self, arr, n):
		cnt = 0
		for i in range(n):
			for j in range(i + cnt, n):
				if arr[j] >= arr[i]:
					cnt = j - i
		return cnt
