def deleteNode(root, key):
	if root == None:
		return root
	if key < root.data:
		root.left = deleteNode(root.left, key)
	elif key > root.data:
		root.right = deleteNode(root.right, key)
	else:
		if root.left == None:
			return root.right
		elif root.right == None:
			return root.left
		tmp = findNext(root.right)
		root.data = tmp
		root.right = deleteNode(root.right, tmp)
	if root == None:
		return root
	root.height = 1 + max(getHeight(root.left), getHeight(root.right))
	bal = getBalance(root)
	if bal > 1 and getBalance(root.left) >= 0:
		return rotateRight(root)
	elif bal > 1 and getBalance(root.left) < 0:
		root.left = rotateLeft(root.left)
		return rotateRight(root)
	elif bal < -1 and getBalance(root.right) <= 0:
		return rotateLeft(root)
	elif bal < -1 and getBalance(root.right) > 0:
		root.right = rotateRight(root.right)
		return rotateLeft(root)
	return root

def getHeight(root):
	if root == None:
		return 0
	return root.height

def getBalance(root):
	if root == None:
		return 0
	return getHeight(root.left) - getHeight(root.right)

def findNext(root):
	while root and root.left:
		root = root.left
	return root.data

def rotateRight(root):
	(x, y, z) = (root, root.left, root.left.left)
	x.left = y.right
	y.right = x
	x.height = 1 + max(getHeight(x.left), getHeight(x.right))
	y.height = 1 + max(getHeight(y.left), getHeight(y.right))
	return y

def rotateLeft(root):
	(x, y, z) = (root, root.right, root.right.right)
	x.right = y.left
	y.left = x
	x.height = 1 + max(getHeight(x.left), getHeight(x.right))
	y.height = 1 + max(getHeight(y.left), getHeight(y.right))
	return y
