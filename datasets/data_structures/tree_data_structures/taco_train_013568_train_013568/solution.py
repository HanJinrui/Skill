class Solution:

	def findMaxSum(self, root):
		ans = [root.data]

		def path(root1):
			if root1 == None:
				return 0
			ls = max(0, path(root1.left))
			rs = max(0, path(root1.right))
			ans[0] = max(ans[0], root1.data + ls + rs)
			return root1.data + max(ls, rs)
		path(root)
		return ans[0]
