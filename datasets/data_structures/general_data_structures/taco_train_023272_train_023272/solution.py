class Solution:

	def shortestUnorderedSubarray(self, a, n):
		a = [int(x) for x in a]
		for index in range(n - 2):
			if a[index] < a[index + 1] > a[index + 2] or a[index] > a[index + 1] < a[index + 2]:
				return 3
		return 0
