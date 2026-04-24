class Solution:

	def nthPoint(self, n):
		arr = [1, 1]
		for _ in range(n):
			arr.append(sum(arr[-2:]) % (10 ** 9 + 7))
		return arr[n]
