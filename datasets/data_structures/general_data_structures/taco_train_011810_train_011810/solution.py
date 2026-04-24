class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, val):
		new_node = Node(val)
		new_node.next = self.head
		self.head = new_node

	def moveZeroes(self):
		k = self.head
		while k and k.next:
			if k.next.data == 0:
				self.push(0)
				if k.next.next:
					k.next = k.next.next
				else:
					k.next = None
			else:
				k = k.next

	def display(self):
		temp = self.head
		while temp is not None:
			print(temp.data, end=' ')
			temp = temp.next
