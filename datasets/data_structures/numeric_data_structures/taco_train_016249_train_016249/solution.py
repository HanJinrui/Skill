class Solution:

	def plusOne(self, digits):
		d = [str(x) for x in digits]
		num = int(''.join(d)) + 1
		return list(map(int, str(num)))
