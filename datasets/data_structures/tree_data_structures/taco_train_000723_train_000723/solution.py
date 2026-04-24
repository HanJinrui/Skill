class Solution:

	def singlevalued(self, root):
		res = 0

		def recur(root):
			nonlocal res
			if not root:
				return set()
			cur = recur(root.left)
			cur.update(recur(root.right))
			cur.add(root.data)
			if len(cur) < 2:
				res += 1
			return cur
		recur(root)
		return res
