def reverseLevelOrder(root):
	q = [root]
	l = []
	while q:
		t = q.pop(0)
		l.append(t.data)
		if t.right:
			q.append(t.right)
		if t.left:
			q.append(t.left)
	return l[::-1]
