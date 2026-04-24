class Solution:

	def repeatedRows(self, arr, m, n):
		l = []
		l1 = []
		for i in range(m):
			if arr[i] in l1:
				l.append(i)
			else:
				l1.append(arr[i])
		return l
