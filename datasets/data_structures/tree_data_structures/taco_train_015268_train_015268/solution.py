from typing import Optional
from collections import deque, defaultdict

class Solution:

	def areAnagrams(self, node1, node2) -> bool:
		freqs1 = []
		dfs(node1, 0, freqs1)
		freqs2 = []
		dfs(node2, 0, freqs2)
		return freqs1 == freqs2

def dfs(n, l, freqs):
	if not n:
		return
	if len(freqs) == l:
		freqs.append(defaultdict(int))
	freqs[l][n.data] += 1
	dfs(n.left, l + 1, freqs)
	dfs(n.right, l + 1, freqs)
