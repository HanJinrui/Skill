class Solution:

	def maximumMatch(self, G):
		(M, N) = (len(G), len(G[0]))
		count = 0
		match = [-1] * N

		def dfs(i):
			for j in range(N):
				if G[i][j] == 1 and j not in vis:
					vis.add(j)
					if match[j] == -1 or dfs(match[j]):
						match[j] = i
						return True
			return False
		for i in range(M):
			vis = set()
			if dfs(i):
				count += 1
		return count
