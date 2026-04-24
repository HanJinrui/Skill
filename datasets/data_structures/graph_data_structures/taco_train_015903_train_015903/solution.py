import random
dy = [-2, -1, 1, 2, -2, -1, 1, 2]
dx = [-1, -2, -2, -1, 1, 2, 2, 1]

class Ponies:
	mat = []
	G = []
	match = []
	used = []

	def dfs(self, v):
		global used
		used.add(v)
		for i in range(len(G[v])):
			u = G[v][i]
			w = match[u]
			if w < 0 or (w not in used and self.dfs(w)):
				match[v] = u
				match[u] = v
				return 1
		return 0

	def bipartiteMatching(self, V):
		global used
		global match
		res = 0
		match = [-1] * 1500
		for v in range(V):
			if match[v] < 0:
				used = set([])
				if self.dfs(v):
					res += 1
		return res

	def maxIndependentSet(self, h, w, V):
		global G
		G = [[] for _ in range(1500)]
		for i in range(h):
			for j in range(w):
				if mat[i][j] == -1:
					continue
				curr = mat[i][j]
				for k in range(8):
					y = i + dy[k]
					x = j + dx[k]
					if y < 0 or y >= h or x < 0 or (x >= w) or (mat[y][x] == -1):
						continue
					G[curr] += [mat[y][x]]
		maximalIndependentSet = V - self.bipartiteMatching(V)
		return maximalIndependentSet

	def solve(self, chessboard):
		global mat
		V = 0
		mat = [[0 for _ in range(50)] for _ in range(50)]
		h = len(chessboard)
		w = len(chessboard[0])
		for i in range(h):
			for j in range(w):
				if chessboard[i][j] == '.':
					V += 1
					mat[i][j] = V
				else:
					mat[i][j] = -1
		return self.maxIndependentSet(h, w, V)
solver = Ponies()
T = int(input())
while T:
	T -= 1
	(h, w) = [int(entry) for entry in input().split(' ')]
	input_mat = []
	for _ in range(h):
		row = input()
		input_mat += [row]
	print(solver.solve(input_mat))
