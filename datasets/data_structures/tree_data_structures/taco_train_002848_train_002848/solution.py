def RemoveHalfNodes(root):
	if not root:
		return
	root.left = RemoveHalfNodes(root.left)
	root.right = RemoveHalfNodes(root.right)
	if root.left and (not root.right):
		return root.left
	if root.right and (not root.left):
		return root.right
	return root
