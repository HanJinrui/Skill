class Solution:

	def minSum(self, arr, n):
		arr.sort()
		num = [0, 0]
		for i in range(n):
			p = i % 2
			num[p] = num[p] * 10 + arr[i]
		return sum(num)
