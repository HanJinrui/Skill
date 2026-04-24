class Solution:

	def compute(self, head):
		if head is None or head.next is None:
			return head
		head.next = self.compute(head.next)
		if head.next.data > head.data:
			return head.next
		else:
			return head
