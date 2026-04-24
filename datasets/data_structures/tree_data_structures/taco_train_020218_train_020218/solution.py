def pathCounts(root):
	d = dict()
	D(d, root, 1)
	for i in d:
		print(i, d[i], end=' $')
	print()

def D(d, root, k):
	if root and (not root.left) and (not root.right):
		if k not in d:
			d[k] = 1
		else:
			d[k] += 1
	if root:
		D(d, root.left, k + 1)
		D(d, root.right, k + 1)
