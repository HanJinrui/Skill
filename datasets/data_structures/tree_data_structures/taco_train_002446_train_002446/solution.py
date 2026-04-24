def findTreeHeight(root):
	if root is None:
		return 0
	if root.left and root.left.right == root:
		return 1
	l = findTreeHeight(root.left)
	r = findTreeHeight(root.right)
	return 1 + max(l, r)
