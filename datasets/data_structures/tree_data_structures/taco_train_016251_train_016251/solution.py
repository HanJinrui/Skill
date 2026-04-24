def buildTree(level, ino):
	return solve(level, 0)

def solve(level1, i):
	root = None
	if i < len(level1):
		root = Node(level1[i])
		root.left = solve(level1, 2 * i + 1)
		root.right = solve(level1, 2 * i + 2)
	return root
