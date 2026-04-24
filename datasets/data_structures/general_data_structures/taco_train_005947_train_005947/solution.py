class Solution:

	def printUnsorted(self, arr, n):
		x = sorted(arr)
		if arr == x:
			return [0, 0]
		l = []
		for i in range(n):
			if arr[i] != x[i]:
				l.append(i)
		return [l[0], l[-1]]
