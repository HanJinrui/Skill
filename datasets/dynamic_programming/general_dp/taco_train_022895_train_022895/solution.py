class Solution:

	def maxLength(self, arr, n):
		p = 0
		n = 0
		f = 0
		for i in arr:
			if i == 0:
				p = 0
				n = 0
			elif i < 0:
				(p, n) = (n + 1 if n else 0, p + 1)
			else:
				(n, p) = (n + 1 if n else 0, p + 1)
			f = max(p, f)
		return f
