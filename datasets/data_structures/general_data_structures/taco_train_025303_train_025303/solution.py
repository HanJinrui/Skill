class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:

	def __init__(self):
		self.head = None

	def push(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			p = self.head
			while p.next:
				p = p.next
			p.next = Node(data)

	def printList(self):
		head = self.head
		l = []
		while head:
			l.append(head.data)
			head = head.next
		print(*l[::-1], end='')
