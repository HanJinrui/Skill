class Solution:

	def checkMirrorTree(self, n, e, A, B):
		d = {}
		for i in range(0, 2 * e, 2):
			d[A[i]] = d.get(A[i], []) + [A[i + 1]]
		for i in range(0, 2 * e, 2):
			if B[i + 1] != d[B[i]].pop():
				return 0
		return 1
