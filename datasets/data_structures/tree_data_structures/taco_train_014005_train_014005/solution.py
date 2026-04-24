def Paths(root):
	res = []

	def t(rt, arr, re):
		if rt is None:
			return
		arr.append(rt.data)
		if rt.left is None and rt.right is None:
			re.append(arr.copy())
		t(rt.left, arr, re)
		t(rt.right, arr, re)
		arr.pop()
	t(root, [], res)
	return res
