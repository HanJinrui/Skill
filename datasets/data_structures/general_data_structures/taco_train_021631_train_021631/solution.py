class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class Solution:

	def sortList(self, head):
		a = []
		while head != None:
			a.append(head.data)
			head = head.next
		a.sort()
		for i in a:
			print(i, end=' ')
