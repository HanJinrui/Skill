class Solution:

	def calc_Sum(self, arr, n, brr, m):
		a = ''
		b = ''
		for i in arr:
			a += str(i)
		for j in brr:
			b += str(j)
		return int(a) + int(b)
