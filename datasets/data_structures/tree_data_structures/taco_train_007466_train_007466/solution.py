class Solution:

	def findMax(self, root):
		temp = root
		while temp.right:
			temp = temp.right
		return temp.data

	def findMin(self, root):
		temp = root
		while temp.left:
			temp = temp.left
		return temp.data
