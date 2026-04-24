class Solution:

	def rearrange(self, head):
		prev = None
		p = head
		while p:
			n = p.next
			if not n:
				break
			p.next = n.next
			n.next = prev
			prev = n
			if not p.next:
				break
			p = p.next
		p.next = prev
		return head
