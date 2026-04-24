def printCorner(root):
	queue = [root]
	while queue:
		n = len(queue)
		for i in range(n):
			cur = queue.pop(0)
			if i == 0 or i == n - 1:
				print(cur.data, end=' ')
			if cur.left:
				queue.append(cur.left)
			if cur.right:
				queue.append(cur.right)
