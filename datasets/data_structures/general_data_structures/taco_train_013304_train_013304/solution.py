class Solution:

	def copyList(self, head):
		d = {None: None}
		curr = head
		while curr:
			d[curr] = Node(curr.data)
			curr = curr.next
		curr = head
		while curr:
			d[curr].next = d[curr.next]
			d[curr].arb = d[curr.arb]
			curr = curr.next
		return d[head]
