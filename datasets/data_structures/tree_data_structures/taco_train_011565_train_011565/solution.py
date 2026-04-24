def fun(root, level, l):
	if root == None:
		return
	if level >= len(l):
		l.append([])
	l[level].append(root.data)
	fun(root.left, level + 1, l)
	fun(root.right, level + 1, l)

def levelOrder(root):
	l = []
	fun(root, 0, l)
	return l
