class Solution:

	def printBoundaryView(self, root):
		if not root:
			return []
		left_bound = []
		bottom_bound = []
		right_bound = []
		runner = root
		if runner.left:
			while runner:
				left_bound.append(runner.data)
				if runner.left:
					runner = runner.left
				else:
					runner = runner.right
		runner = root

		def dfs(node):
			if not node:
				return
			if not node.left and (not node.right):
				bottom_bound.append(node.data)
			dfs(node.left)
			dfs(node.right)
		dfs(runner)
		runner = root
		if runner.right:
			while runner:
				right_bound.append(runner.data)
				if runner.right:
					runner = runner.right
				else:
					runner = runner.left
		if left_bound == [] and right_bound == []:
			return [root.data]
		elif left_bound == []:
			return [root.data] + bottom_bound[:] + right_bound[-2:0:-1]
		return left_bound + bottom_bound[1:] + right_bound[-2:0:-1]
