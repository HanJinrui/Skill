class Solution:

	def removeAllDuplicates(self, head):
		(t, l, d) = (head, [], {})
		while t:
			if t.data in d:
				if t.data in l:
					l.remove(t.data)
			else:
				d[t.data] = 1
				l.append(t.data)
			t = t.next
		h = LinkedList()
		for i in l:
			h.append(i)
		return h.head
