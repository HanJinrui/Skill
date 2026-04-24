class Solution:

	def getSubstringWithEqual012(self, Str):
		a = 0
		b = 0
		c = 0
		d = {}
		d[0, 0] = 1
		ans = 0
		for i in Str:
			if i == '0':
				a += 1
			elif i == '1':
				b += 1
			else:
				c += 1
			temp = (a - b, a - c)
			if temp in d:
				ans += d[temp]
				d[temp] += 1
			else:
				d[temp] = 1
		return ans
