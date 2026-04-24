def sumLeaf(root):
	if root:
		if root.left or root.right:
			return sumLeaf(root.left) + sumLeaf(root.right)
		return root.data
	return 0
