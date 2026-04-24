class Solution:

	def bTreeToClist(self, root):
		dummy = Node(-1)
		tail = dummy

		def dfs(root):
			nonlocal tail
			if root:
				dfs(root.left)
				tail.right = root
				root.left = tail
				tail = tail.right
				dfs(root.right)
		dfs(root)
		dummy.right.left = tail
		tail.right = dummy.right
		return dummy.right
