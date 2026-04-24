class Solution:

	def findSum(self, a, b):
		a = int(''.join(map(str, a)))
		b = int(''.join(map(str, b)))
		return [*str(a + b)]
