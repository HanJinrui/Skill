def constructTree(pre, preLN, n):

	def _solve(i):
		nd = Node(pre[i])
		if preLN[i] == 'N':
			(nd.left, i) = _solve(i + 1)
			(nd.right, i) = _solve(i + 1)
		return (nd, i)
	(head, _) = _solve(0)
	return head
