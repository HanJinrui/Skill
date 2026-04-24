class Solution:

	def reverse(self, head, k):
		c = 0
		prev = None
		cur = head
		while cur and c < k:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
			c += 1
		if next:
			head.next = self.reverse(next, k)
		return prev
