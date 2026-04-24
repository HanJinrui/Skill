class Solution:

	def sumoflength(self, arr, n):
		counter = 0
		for i in range(n):
			h = {}
			for j in range(i, n):
				if arr[j] not in h:
					h[arr[j]] = 1
					counter += len(h)
				else:
					break
		return counter
