def fun(root):
	global head
	if root == None:
		return None
	if root.left == None and root.right == None:
		root.right = head
		if head != None:
			head.left = root
		head = root
		return None
	root.right = fun(root.right)
	root.left = fun(root.left)
	return root

def convertToDLL(root):
	global head
	head = None
	root = fun(root)
