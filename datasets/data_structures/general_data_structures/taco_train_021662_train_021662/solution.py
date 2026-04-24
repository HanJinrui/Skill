class Solution:

	def rotate(self, h, k):
		n = h
		while n.next:
			n = n.next
		for i in range(k):
			n.next = h
			n = n.next
			h = h.next
			n.next = None
		return h
