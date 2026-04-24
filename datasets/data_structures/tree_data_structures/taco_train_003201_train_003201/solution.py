def noSibling(root):
	ans = []

	def help(root):
		if root == None:
			return
		if root.left and (not root.right):
			ans.append(root.left.data)
		if root.right and (not root.left):
			ans.append(root.right.data)
		help(root.left)
		help(root.right)
	help(root)
	return sorted(ans) if ans else [-1]
