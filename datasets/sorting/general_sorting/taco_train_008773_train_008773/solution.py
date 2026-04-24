class Solution:

	def findMaxRow(self, mat, N):
		l = []
		for i in mat:
			l.append(i.count(1))
		return (l.index(max(l)), max(l))
