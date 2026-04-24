class Solution:

	def transform(self, Str):
		res = ''
		for x in Str:
			if x not in 'aeiouAEIOU':
				res += '#' + x
		return res.swapcase() if res else -1
