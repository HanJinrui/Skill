class Solution:

	def Learning(self, arr, n):
		pos = neg = zero = 0
		for i in arr:
			if i == 0:
				zero += 1
			elif i > 0:
				pos += 1
			else:
				neg += 1
		pos = n / pos
		neg = n / neg
		zero = n / zero
		return ('%g' % pos, '%g' % neg, '%g' % zero)
