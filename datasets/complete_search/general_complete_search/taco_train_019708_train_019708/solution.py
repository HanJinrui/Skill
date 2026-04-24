def graphColoring(g, m, n):

	def isSafe(i, c):
		for j in range(n):
			if g[i][j] and col[j] == c:
				return False
		return True
	col = [-1] * n

	def dfs(i):
		if i == n:
			return True
		for c in range(m):
			if isSafe(i, c):
				temp = col[i]
				col[i] = c
				if dfs(i + 1):
					return True
				col[i] = temp
		return False
	return dfs(0)
