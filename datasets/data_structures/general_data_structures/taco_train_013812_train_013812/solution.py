class Solution:

	def countOddEven(self, arr, n):
		l = [x for x in arr if x % 2 == 0]
		print(n - len(l), len(l))
