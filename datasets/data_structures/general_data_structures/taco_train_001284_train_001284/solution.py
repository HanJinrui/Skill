class Solution:

	def reverseBetween(self, head, m, n):
		if not head:
			return None
		node = ListNode(0)
		node.next = head
		pre = node
		cur = node.__next__
		for i in range(m - 1):
			pre = pre.__next__
			cur = cur.__next__
		for i in range(n - m):
			tmp = cur.__next__
			cur.next = tmp.__next__
			tmp.next = pre.__next__
			pre.next = tmp
		return node.__next__
