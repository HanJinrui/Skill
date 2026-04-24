class Solution:

	def maximumValue(self, node):
		l = []

		def find(node, lv):
			if node is None:
				return
			if lv == len(l):
				l.append(node.data)
			else:
				l[lv] = max(l[lv], node.data)
			find(node.left, lv + 1)
			find(node.right, lv + 1)
		find(node, 0)
		return l
