class Solution:

	def verticalSum(self, root):

		def solver(root, i=501):
			if not root:
				return
			if ans[i] == None:
				ans[i] = 0
			ans[i] += root.data
			solver(root.left, i - 1)
			solver(root.right, i + 1)
		ans = [None] * 1002
		solver(root)
		return [i for i in ans if i is not None]
