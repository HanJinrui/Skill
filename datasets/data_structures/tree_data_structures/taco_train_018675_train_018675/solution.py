def fun(root, level, ds):
	if root == None:
		return
	if len(ds) == level:
		ds.append(root.data)
	fun(root.left, level + 1, ds)
	fun(root.right, level + 1, ds)

def LeftView(root):
	ds = []
	fun(root, 0, ds)
	return ds
