def numberOfCells(n, m, r, c, u, d, mat):
	if mat[r][c] == '#':
		return 0
	q = []
	count = 1
	q.append([r, c, 0, 0])
	mat[r][c] = 1
	while q:
		temp = q.pop(0)
		x = temp[0]
		y = temp[1]
		up = temp[2]
		down = temp[3]
		if y - 1 >= 0 and mat[x][y - 1] == '.':
			count += 1
			q.append([x, y - 1, up, down])
			mat[x][y - 1] = 1
		if y + 1 < m and mat[x][y + 1] == '.':
			count += 1
			q.append([x, y + 1, up, down])
			mat[x][y + 1] = 1
		if x - 1 >= 0 and up != u and (mat[x - 1][y] == '.'):
			count += 1
			q.append([x - 1, y, up + 1, down])
			mat[x - 1][y] = 1
		if x + 1 < n and down != d and (mat[x + 1][y] == '.'):
			count += 1
			q.append([x + 1, y, up, down + 1])
			mat[x + 1][y] = 1
	return count
