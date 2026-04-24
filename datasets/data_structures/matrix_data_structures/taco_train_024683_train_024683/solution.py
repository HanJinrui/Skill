class Solution:

	def isValid(self, mat):
		h = set()
		for i in range(9):
			for j in range(9):
				char = str(mat[i][j])
				if int(char) != 0:
					if (i, char) in h or (char, j) in h or (char, i // 3, j // 3) in h:
						return 0
					h.add((i, char))
					h.add((char, j))
					h.add((char, i // 3, j // 3))
		return 1
