def slove(root, lvl, d):
	if root is None:
		return
	if lvl not in d:
		d[lvl] = root.data
	else:
		d[lvl] += root.data
	slove(root.left, lvl + 1, d)
	slove(root.right, lvl + 1, d)

class Solution:

	def maxLevelSum(self, root):
		d = {}
		slove(root, 0, d)
		return max(d.values())
