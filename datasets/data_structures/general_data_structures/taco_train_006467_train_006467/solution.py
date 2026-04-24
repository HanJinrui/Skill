from typing import Optional

class Solution:

	def moveToFront(self, head: Optional['Node']) -> Optional['Node']:
		prev = head
		itr = head
		while itr.next:
			prev = itr
			itr = itr.next
		itr.next = head
		prev.next = None
		return itr
