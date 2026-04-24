from typing import Optional

class Solution:

	def reverse(self, head: Optional['Node'], k: int) -> Optional['Node']:
		l = []
		p = head
		while p:
			l.append(p.data)
			p = p.next
		l = l[:k][::-1] + l[:k - 1:-1]
		head = Node(0)
		curr = head
		for i in l:
			curr.next = Node(i)
			curr = curr.next
		return head.next
