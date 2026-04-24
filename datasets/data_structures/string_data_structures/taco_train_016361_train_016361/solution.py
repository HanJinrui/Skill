class Solution:

	def modifyArray(self, arr, n):
		res = [-1] * n
		for i in arr:
			if i >= 0:
				res[i] = i
		return res
