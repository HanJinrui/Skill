class Solution:

	def MaximumIntegerValue(self, S):
		num = 0
		for s in S:
			num = max(num * int(s), num + int(s))
		return num
