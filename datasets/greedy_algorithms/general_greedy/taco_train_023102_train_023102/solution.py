class Solution:

	def smallestNumber(self, S, D):
		if S > D * 9:
			return '-1'
		S -= 1
		res = 10 ** (D - 1)
		d = 1
		while S > 0:
			res += d * min(S, 9)
			S -= min(S, 9)
			d *= 10
		return str(res)
