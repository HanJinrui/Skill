def sumBT(root):
	if not root:
		return 0
	return root.data + sumBT(root.left) + sumBT(root.right)
