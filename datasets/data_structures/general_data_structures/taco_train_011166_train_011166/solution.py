class Solution:

	def deleteNode(self, head, x):
		temp = head
		count = 2
		if x == 1:
			temp.next.prev = None
			head = temp.next
		else:
			while count < x:
				temp = temp.next
				count += 1
			temp.next = temp.next.next
