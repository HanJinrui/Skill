from typing import List

class Solution:

	def solve(self, N: int, p: List[int]) -> int:
		adj = [[] for _ in range(N)]
		for i in range(1, N):
			adj[p[i]].append(i)
		ans = 1 if len(adj[0]) == 1 else 0
		for a in adj:
			if not a:
				ans += 1
		return max(N - 1 - ans, 0)
