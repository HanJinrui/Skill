class Solution:

	def endPoints(self, m, r, c):
		cl = 0
		i = j = k = l = 0
		while 0 <= i < r and 0 <= j < c:
			k = i
			l = j
			if m[i][j] == 1:
				m[i][j] = 0
				cl += 1
			if cl % 4 == 0:
				j += 1
			if cl % 4 == 1:
				i += 1
			if cl % 4 == 2:
				j -= 1
			if cl % 4 == 3:
				i -= 1
		return [k, l]
