from typing import List

class Solution:

	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		from collections import deque
		for j in range(V):
			q = deque()
			vis = [False] * V
			q.append(j)
			while q:
				u = q.popleft()
				vis[u] = True
				for i in adj[u]:
					if q.count(i) == 1:
						return True
					if vis[i] == False:
						q.append(i)
		return False
