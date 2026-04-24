class Solution:

	def addTwoLists(self, first, second):
		f = ''
		s = ''
		curr = first
		while curr:
			f += str(curr.data)
			curr = curr.next
		curr = second
		while curr:
			s += str(curr.data)
			curr = curr.next
		f_s = int(f) + int(s)
		head = None
		for i in str(f_s)[::-1]:
			temp = Node(i)
			temp.next = head
			head = temp
		return head
