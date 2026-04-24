class Solution:

	def sumOfLongRootToLeafPath(self, root):
		return findSum(root, [0, 0], 0, 0)[0]

def findSum(root, res, l, s):
	if root == None:
		return res
	s += root.data
	if l > res[1]:
		res[1] = l
		res[0] = s
	elif l == res[1]:
		res[0] = max(res[0], s)
	findSum(root.left, res, l + 1, s)
	findSum(root.right, res, l + 1, s)
	return res
