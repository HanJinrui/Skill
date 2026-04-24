class Solution:

	def deleteAlt(self, head):
		while head and head.next:
			head.next = head.next.next
			head = head.next
