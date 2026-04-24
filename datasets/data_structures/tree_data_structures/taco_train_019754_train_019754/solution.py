def kthAncestor(root, k, node):
	arr = []

	def sol(root, node):
		if root is None:
			return False
		arr.append(root)
		if root.data == node:
			return True
		if sol(root.left, node) or sol(root.right, node):
			return True
		arr.pop()
	sol(root, node)
	if k > len(arr) - 1:
		return -1
	else:
		return arr[len(arr) - k - 1].data
