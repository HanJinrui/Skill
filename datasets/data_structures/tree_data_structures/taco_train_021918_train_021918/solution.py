class Solution:

	def partyHouse(self, n, adj):

		def dfs(i, prev, cost):
			mx[0] = max(mx[0], cost)
			for e in adj[i]:
				if e != prev:
					dfs(e, i, cost + 1)
		ans = 1000
		for i in range(1, n + 1):
			mx = [0]
			dfs(i, -1, 0)
			ans = min(ans, mx[0])
		return ans
