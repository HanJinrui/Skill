class Solution:

	def insertAtBegining(self, head, x):
		n = Node(x)
		n.next = head
		return n

	def insertAtEnd(self, head, x):
		n = Node(x)
		if not head:
			return n
		p = head
		while p.next:
			p = p.next
		p.next = n
		return head
