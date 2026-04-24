class Solution:

	def zigzag(self, head):
		flg = 1
		h = head
		while h.next:
			if flg:
				if h.data > h.next.data:
					(h.data, h.next.data) = (h.next.data, h.data)
			elif h.data < h.next.data:
				(h.data, h.next.data) = (h.next.data, h.data)
			h = h.next
			flg = 1 - flg
		return head
