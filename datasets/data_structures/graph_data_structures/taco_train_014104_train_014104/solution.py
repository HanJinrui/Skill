class Solution:

	def tarjans(self, V, adj):
		stack = []
		visit = [0] * V

		def fun(i):
			visit[i] = 1
			for j in adj[i]:
				if visit[j] == 0:
					fun(j)
			stack.append(i)
		for i in range(V):
			if visit[i] == 0:
				fun(i)
		ans = []
		visit = [0] * V
		new = [[] for _ in range(V)]
		for i in range(V):
			for k in adj[i]:
				new[k].append(i)

		def fun1(i, lis):
			visit[i] = 1
			lis.append(i)
			for j in new[i]:
				if visit[j] == 0:
					fun1(j, lis)
			return lis
		while stack:
			t = stack.pop()
			if visit[t] == 0:
				l = fun1(t, [])
				l.sort()
				ans.append(l)
		ans.sort()
		return ans
