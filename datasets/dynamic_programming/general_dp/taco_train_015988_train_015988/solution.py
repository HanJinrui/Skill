class Solution:

	def ZigZagMaxLength(self, l):
		u = 0
		d = 0
		n = len(l)
		for i in range(n - 1):
			if l[i + 1] > l[i]:
				u = d + 1
			elif l[i + 1] < l[i]:
				d = u + 1
		return max(u, d) + 1
