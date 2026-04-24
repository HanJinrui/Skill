class Solution:

	def divide(self, N, head):
		a = []
		b = []
		c = []
		while head != None:
			a.append(head.data)
			head = head.next
		for i in a:
			if i % 2 == 0:
				b.append(i)
			else:
				c.append(i)
		x = b + c
		for j in x:
			print(j, end=' ')
