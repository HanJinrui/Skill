class Solution:

	def endPoints(self, matrix, m, n):
		change = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		ind = 0
		i = j = 0
		while i > -1 and i < m and (j > -1) and (j < n):
			if matrix[i][j] == 1:
				ind = (ind + 1) % 4
				matrix[i][j] = 0
			cell = [i, j]
			i += change[ind][0]
			j += change[ind][1]
		return cell
