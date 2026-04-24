from collections import defaultdict as dc

class Solution:

	def firingEmployees(self, a, n):

		def prime(x):
			for i in range(2, int(x ** 0.5) + 1):
				if x % i == 0:
					return 0
			return 1
		adj = dc(list)
		for i in range(n):
			if a[i] == 0:
				root = i + 1
			adj[a[i]].append(i + 1)
		nl = []
		cl = adj[root]
		dp = 1
		ans = 0
		while cl:
			x = cl.pop()
			nl += adj[x]
			if prime(x + dp):
				ans += 1
			if not cl:
				cl = nl[:]
				nl = []
				dp += 1
		return ans
