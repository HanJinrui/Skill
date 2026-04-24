class Solution:

	def sumClosest(self, a, x):
		(sm, diff, i, j) = (0, float('inf'), 0, len(a) - 1)
		while i < j:
			sm = a[i] + a[j]
			if abs(x - sm) < diff:
				diff = abs(x - sm)
				m = [a[i], a[j]]
			elif sm > x:
				j -= 1
			else:
				i += 1
		return m
