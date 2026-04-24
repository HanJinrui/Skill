class Solution:

	def connect(self, root):
		q = []
		ans = []
		q.append(root)
		while q:
			n = len(q)
			a = []
			for j in range(n):
				node = q.pop(0)
				a.append(node)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			ans.append(a)
		for i in ans:
			for j in range(len(i)):
				if j + 1 < len(i):
					i[j].nextRight = i[j + 1]
				else:
					i[j].nextRight = None
