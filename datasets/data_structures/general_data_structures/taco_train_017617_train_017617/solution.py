class Solution:

	def reorderList(self, head):
		slow = fast = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		l2 = slow.next
		slow.next = None
		prev = None
		while l2:
			nextt = l2.next
			l2.next = prev
			prev = l2
			l2 = nextt
		l1 = head
		l2 = prev
		while l1 and l2:
			nextt1 = l1.next
			nextt2 = l2.next
			l1.next = l2
			l2.next = nextt1
			l1 = nextt1
			l2 = nextt2
