def solve(row, col, mat):
	if row >= len(mat) or col >= len(mat[0]):
		return None
	cur = Node(mat[row][col])
	cur.right = solve(row, col + 1, mat)
	cur.down = solve(row + 1, col, mat)
	return cur

def constructLinkedMatrix(mat, n):
	return solve(0, 0, mat)
