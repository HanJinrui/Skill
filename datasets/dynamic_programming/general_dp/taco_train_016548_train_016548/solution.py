from typing import List

class Solution:

	def makeChanges(self, n, k, target, coins):
		table = [[False] * (k + 1) for _ in range(target + 1)]
		table[0][0] = True
		for c in coins:
			for i in range(c, target + 1):
				for j in range(1, k + 1):
					table[i][j] |= table[i - c][j - 1]
		return table[target][k]
