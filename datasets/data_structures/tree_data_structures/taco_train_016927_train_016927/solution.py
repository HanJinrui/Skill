class Solution:

	def countBT(self, h):
		arr = [1, 3]
		for i in range(h):
			arr.append(((arr[-1] + arr[-2]) ** 2 - arr[-2] ** 2) % (10 ** 9 + 7))
		return arr[h - 1]
