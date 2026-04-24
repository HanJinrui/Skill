def reverseAlternate(root):

	def dfs(n1, n2, level):
		if not n1:
			return
		if level % 2:
			(n1.data, n2.data) = (n2.data, n1.data)
		dfs(n1.left, n2.right, level + 1)
		dfs(n1.right, n2.left, level + 1)
	dfs(root.left, root.right, 1)
	return root
