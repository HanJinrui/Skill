def deletionBT(root, key):
	keyNode = None
	q = [root]
	while q != []:
		t = q.pop(0)
		if t.data == key:
			keyNode = t
		if t.left:
			last = t
			q.append(t.left)
		if t.right:
			last = t
			q.append(t.right)
	if keyNode:
		keyNode.data = t.data
		if last.left == t:
			last.left = None
		else:
			last.right = None
