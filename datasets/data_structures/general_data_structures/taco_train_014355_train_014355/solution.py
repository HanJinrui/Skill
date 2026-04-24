class Solution:

	def segregate(self, head):
		a = []
		while head != None:
			a.append(head.data)
			head = head.next
		a.sort()
		for i in a:
			print(i, end=' ')
