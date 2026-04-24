def maxNodeLevel(root):
	q = [root]
	res = 0
	mx = 0
	lev = 0
	while q:
		l = len(q)
		if l > mx:
			mx = l
			res = lev
		for i in range(l):
			p = q.pop(0)
			if p.left:
				q.append(p.left)
			if p.right:
				q.append(p.right)
		lev += 1
	return res
