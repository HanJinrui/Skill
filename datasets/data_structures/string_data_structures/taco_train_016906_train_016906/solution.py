class Solution:

	def convertRoman(self, n):
		n = int(n)
		z = ''
		x = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		y = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
		for i in range(13):
			while n >= x[i]:
				n = n - x[i]
				z += y[i]
		return z
