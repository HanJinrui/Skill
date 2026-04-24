class Solution:

	def countPaths(self, V, adj, source, destination):
		l = [0]

		def f(s):
			if s == destination:
				l[0] += 1
				return
			for i in adj[s]:
				f(i)
		f(source)
		return l[0]
