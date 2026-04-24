class Solution:

	def deleteNode(self, curr):
		curr.data = curr.next.data
		curr.next = curr.next.next
