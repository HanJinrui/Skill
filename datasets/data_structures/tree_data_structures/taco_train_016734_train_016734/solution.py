class Solution:

	def NumberOFTurns(self, root, first, second):

		def LCA(node, node1, node2):
			if not node:
				return None
			if node.data == node1 or node.data == node2:
				return node
			a = LCA(node.left, node1, node2)
			b = LCA(node.right, node1, node2)
			if a and b:
				return node
			return a if a else b
		lca = LCA(root, first, second)

		def path(root, node, s):
			if not root:
				return ''
			if root.data == node:
				return s
			return path(root.left, node, s + 'L') or path(root.right, node, s + 'R')
		l = path(lca, first, '')
		r = path(lca, second, '')
		l = l[::-1]
		total = l + r
		ans = 0
		for i in range(1, len(total)):
			if total[i] != total[i - 1]:
				ans += 1
		return ans
