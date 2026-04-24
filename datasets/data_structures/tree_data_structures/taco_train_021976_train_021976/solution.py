from collections import defaultdict

class Solution:

	def sum_at_distK(self, root, target, k):
		d = defaultdict(list)

		def helper(root):
			if root is None:
				return
			if root.left:
				d[root.data].append(root.left.data)
				d[root.left.data].append(root.data)
				helper(root.left)
			if root.right:
				d[root.data].append(root.right.data)
				d[root.right.data].append(root.data)
				helper(root.right)
		helper(root)
		if target not in d:
			return -1
		sm = 0
		visited = {}

		def dfs(node, level):
			nonlocal k, visited, sm, d
			if level > k:
				return
			if node not in visited:
				sm = sm + node
			visited[node] = True
			for i in d[node]:
				dfs(i, level + 1)
		dfs(target, 0)
		return sm
