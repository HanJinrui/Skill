class Solution:

	def sortedInsert(self, head, data):
		if head.data > data:
			p = head
			while head.next != p:
				head = head.next
			p = head.next
			head.next = Node(data)
			head.next.next = p
			return head.next
		h = head
		while head.next.data <= data:
			head = head.next
		p = head.next
		head.next = Node(data)
		head.next.next = p
		return h
