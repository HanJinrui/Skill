class Solution:

	def removeDuplicates(self, head):
		c = head
		p = None
		d = {}
		while c:
			if c.data in d:
				p.next = c.next
				c = None
			else:
				d[c.data] = 1
				p = c
			c = p.next
		return head
