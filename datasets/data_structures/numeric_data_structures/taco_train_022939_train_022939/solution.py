class Solution:

	def arrange(self, arr, n):
		arr[:] = [arr[elem] for elem in arr]
