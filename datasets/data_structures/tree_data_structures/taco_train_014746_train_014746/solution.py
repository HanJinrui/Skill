def preorder(root):
	if root == None:
		return []
	return [root.data] + preorder(root.left) + preorder(root.right)
