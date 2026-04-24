class Solution:

	def pairWiseSwap(self, head):
		if not (head and head.next):
			return head
		(head.next.next, head.next, head) = (head, self.pairWiseSwap(head=head.next.next), head.next)
		return head
