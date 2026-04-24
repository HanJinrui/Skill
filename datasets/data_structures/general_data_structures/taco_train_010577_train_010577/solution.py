class Solution:

	def compute(self, a, n):
		l = [0] * n
		l[0] = 1
		for i in range(1, n):
			if a[i] >= a[i - 1]:
				l[i] = l[i - 1] + 1
			else:
				l[i] = 1
		return max(l)
