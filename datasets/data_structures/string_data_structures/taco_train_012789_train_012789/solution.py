class Solution:

	def countSubstringWithEqualEnds(self, s):
		a = set(s)
		sum = 0
		for i in a:
			c = s.count(i)
			sum += int(c * (c + 1) / 2)
		return sum
