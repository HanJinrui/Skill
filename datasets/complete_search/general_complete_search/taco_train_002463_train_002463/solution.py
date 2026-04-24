class Solution:

	def nQueen(self, n):

		def dfs(cols, neg, pos):
			p = len(cols)
			if p == n:
				result.append(list(map(lambda x: x + 1, cols)))
				return
			for i in range(n):
				if i not in cols and p - i not in neg and (p + i not in pos):
					dfs(cols + [i], neg + [p - i], pos + [p + i])
		result = []
		dfs([], [], [])
		return result
