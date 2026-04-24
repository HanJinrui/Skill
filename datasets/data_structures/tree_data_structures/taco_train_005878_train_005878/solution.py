from collections import defaultdict

class Solution:

	def maximumWeight(self, n, edges, q, queries):

		def par(i):
			while p[i] != i:
				i = p[i]
			return i

		def union(i, j):
			i = par(i)
			j = par(j)
			if i < j:
				p[i] = j
				count[j] += count[i]
			else:
				p[j] = i
				count[i] += count[j]
		edges += [['_', '_', i] for i in queries]
		edges.sort(key=lambda i: i[-1])
		ans = 0
		p = [i for i in range(n)]
		count = [1 for i in range(n)]
		res = defaultdict(int)
		for (a, b, c) in edges:
			if a != '_':
				a -= 1
				b -= 1
				ans += count[par(a)] * count[par(b)]
				union(a, b)
			res[c] = ans
		return [res[i] for i in queries]
