class Solution:

	def createTree(self, p, N):
		l = []
		for i in range(N):
			l.append(Node(i))
		for i in range(N):
			if p[i] != -1:
				if l[p[i]].left is None:
					l[p[i]].left = l[i]
				else:
					l[p[i]].right = l[i]
			else:
				g = i
		return l[g]
