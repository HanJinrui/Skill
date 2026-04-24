class Solution:

	def fun(i, arr):
		k = arr[0] % i
		for j in arr:
			if j % i != k:
				return False
		return True

	def printEqualModNumbers(self, arr, n):
		if n == 1:
			return -1
		a = max(arr)
		res = 0
		for i in range(1, a + 1):
			if Solution.fun(i, arr):
				res += 1
		if res == 0:
			return -1
		else:
			return res
