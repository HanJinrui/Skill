def KDistance(root, k):
	A = []
	x(root, k, A)
	return A

def x(root, k, A):
	if root is None:
		return
	if k == 0:
		A.append(root.data)
	x(root.left, k - 1, A)
	x(root.right, k - 1, A)
