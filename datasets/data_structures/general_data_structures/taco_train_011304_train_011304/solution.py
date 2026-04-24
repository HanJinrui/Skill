class Solution:

	def addOne(self, head):
		a = ''
		temp = head
		while temp:
			a += str(temp.data)
			temp = temp.next
		a = int(a)
		return Node(a + 1)
