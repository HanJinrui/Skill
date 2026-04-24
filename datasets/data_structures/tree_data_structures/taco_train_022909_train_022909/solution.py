def fun(root, n, l):
	if root == None:
		return
	if n not in l:
		l.append(n)
	fun(root.left, n - 1, l)
	fun(root.right, n + 1, l)

def verticalWidth(root):
	l = []
	fun(root, 0, l)
	return len(l)
