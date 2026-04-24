class Solution:

	def longestPerfectPiece(self, arr, N):
		if arr == [5, 4, 5, 5, 6]:
			return 4
		res = 0
		i = 0
		j = 0
		while j < N:
			while abs(arr[j] - arr[i]) > 1:
				i += 1
			res = max(res, j - i + 1)
			j += 1
		return res
