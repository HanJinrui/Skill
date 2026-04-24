class Solution:

	def lookandsay(self, n):
		if n == 1:
			return '1'
		p = self.lookandsay(n - 1)
		ans = ''
		c = 1
		for i in range(len(p)):
			if i == len(p) - 1 or p[i] != p[i + 1]:
				ans += str(c) + p[i]
				c = 1
			else:
				c += 1
		return ans
