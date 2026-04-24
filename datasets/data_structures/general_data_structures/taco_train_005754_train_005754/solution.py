class Solution:

	def partition(self, head, x):
		l = []
		while head:
			l.append(head.data)
			head = head.next
		a = []
		b = []
		c = []
		for i in l:
			if i < x:
				a.append(i)
			elif i == x:
				b.append(i)
			else:
				c.append(i)
		for i in a + b + c:
			print(i, end=' ')
