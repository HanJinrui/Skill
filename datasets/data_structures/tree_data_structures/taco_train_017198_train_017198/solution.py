class Solution:

	def evalTree(self, root):
		if root.left == root.right == None:
			return str(root.data)
		return int(eval(str(self.evalTree(root.left)) + str(root.data) + str(str(self.evalTree(root.right)))))
