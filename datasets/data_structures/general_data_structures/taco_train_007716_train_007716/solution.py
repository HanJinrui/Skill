class Solution:

	def update(self, a, n, u, k):
		for i in range(0, k):
			a[u[i] - 1] += 1
		for i in range(1, n):
			a[i] += a[i - 1]
