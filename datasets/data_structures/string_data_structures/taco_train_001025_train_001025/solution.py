class Solution:

	def maxSubStr(self, str):
		p = 0
		res = 0
		for i in str:
			if i == '1':
				p -= 1
			else:
				p += 1
			if p == 0:
				res += 1
		if p != 0:
			return -1
		return res
