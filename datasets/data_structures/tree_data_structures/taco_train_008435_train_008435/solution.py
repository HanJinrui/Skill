def IsFoldable(root):
	return ans(root, root)

def ans(x, y):
	if x == None and y == None:
		return True
	elif x == None and y != None or (x != None and y == None):
		return False
	return ans(x.left, y.right) and ans(x.right, y.left)
