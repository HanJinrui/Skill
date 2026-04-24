class Solution:

	def RevDelMST(self, arr, v, e):
		edges = []
		graph = [[0 for i in range(v)] for i in range(v)]
		for i in range(3, len(arr) + 1, 3):
			edges.append(arr[i - 3:i])
			graph[arr[i - 3]][arr[i - 2]] = 1
			graph[arr[i - 2]][arr[i - 3]] = 1

		def dfs(z, visited):
			visited[z] = 1
			for i in range(v):
				if graph[z][i] == 1 and (not visited[i]):
					dfs(i, visited)

		def connected():
			visited = [0] * v
			dfs(0, visited)
			for i in range(v):
				if visited[i] == 0:
					return 0
			return 1
		edges = sorted(edges, key=lambda x: x[2])
		ans = 0
		total = 0
		while edges:
			(u, e, w) = edges.pop()
			total += w
			graph[u][e] = 0
			graph[e][u] = 0
			if connected():
				ans += w
			else:
				graph[u][e] = 1
				graph[e][u] = 1
		return total - ans
