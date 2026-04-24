def getSize(node):
	return 1 + getSize(node.left) + getSize(node.right) if node else 0
