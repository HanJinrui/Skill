class Solution:

	def sortedInsert(self, head, key):
		l = []
		h = head
		while h:
			l.append(h.data)
			h = h.next
		l.append(key)
		l.sort()
		a = b = Node(-1)
		for i in l:
			a.next = Node(i)
			a = a.next
		return b.next
