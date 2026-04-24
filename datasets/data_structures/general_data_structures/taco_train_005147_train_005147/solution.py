class Solution:

	def prank(self, a, n):
		copy_a = a.copy()
		for i in range(n):
			a[i] = copy_a[a[i]]
