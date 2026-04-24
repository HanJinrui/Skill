class Solution:

	def distance(self, x, y):
		res = 0
		while x != y:
			if x > y:
				x //= 2
			else:
				y //= 2
			res += 1
		return res
