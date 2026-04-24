class Solution:

	def rearrangeArray(self, arr, n):
		arr.sort()
		i = 1
		for _ in range(n // 2):
			arr.insert(i, arr.pop())
			i += 2
		return arr
