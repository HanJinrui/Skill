class Solution:

	def processqueries(self, arr, n, m, q):
		left = [0] * n
		right = [0] * n
		right[n - 1] = n - 1
		last = 0
		for i in range(1, n):
			if arr[i - 1] < arr[i]:
				last = i
			left[i] = last
		last = n - 1
		for i in range(n - 2, -1, -1):
			if arr[i] > arr[i + 1]:
				last = i
			right[i] = last
		op = []
		for (i, j) in q:
			op.append('Yes' if right[i] >= left[j] else 'No')
		return op
