class Solution:

	def lcsK(self, k, st):
		st = st + st
		n = len(st)
		here = 0
		mx = 0
		for i in range(n):
			if st[i] == '0':
				here += 1
			else:
				here = 0
			mx = max(mx, here)
		if mx == n:
			return mx * k // 2
		else:
			return mx
