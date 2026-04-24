def treePathSum(root, data=0):
	if root == None:
		return 0
	data = data * 10 + root.data
	if root.left == None and root.right == None:
		return data
	return treePathSum(root.left, data) + treePathSum(root.right, data)
