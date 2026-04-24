class Solution:

	def reverseList(self, head):
		(p, c) = (None, head)
		while c:
			n = c.next
			c.next = p
			(p, c) = (c, n)
		return p
