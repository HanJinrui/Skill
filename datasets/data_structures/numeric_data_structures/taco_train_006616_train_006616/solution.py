class Solution:

	def checkFib(self, arr, N):
		x = [0, 1, 1]
		while sum(x[-2:]) <= max(arr):
			x.append(sum(x[-2:]))
		return len([i for i in arr if i in x])
