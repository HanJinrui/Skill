def slove(r1, r2):
	if r1 is None and r2 is None:
		return True
	if r1 is None or r2 is None:
		return False
	if r1.data != r2.data:
		return False
	return slove(r1.left, r2.left) and slove(r1.right, r2.right) or (slove(r1.left, r2.right) and slove(r1.right, r2.left))

class Solution:

	def isIsomorphic(self, root1, root2):
		return slove(root1, root2)
