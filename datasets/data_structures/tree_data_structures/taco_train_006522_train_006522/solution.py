def printKDistantfromLeaf(root, k):
	s = set()

	def solve(root, ans):
		if not root:
			return
		if not root.left and (not root.right):
			if len(ans) >= k:
				s.add(ans[len(ans) - k])
			return
		ans.append(root)
		solve(root.left, ans)
		solve(root.right, ans)
		ans.pop()
		return
	solve(root, [])
	return len(s)
