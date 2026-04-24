class Solution:

	def findMid(self, head):
		p = head
		q = head
		while q and q.next:
			p = p.next
			q = q.next.next
		return p.data
