def postOrder(root):
	if root is None:
		return []
	return postOrder(root.left) + postOrder(root.right) + [root.data]
