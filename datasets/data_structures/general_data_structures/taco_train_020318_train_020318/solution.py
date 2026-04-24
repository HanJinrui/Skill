class Solution:

	def rearrangeEvenOdd(self, head):
		dummy = even = head
		node = odd = head.next
		while even.next and odd.next:
			even.next = odd.next
			even = even.next
			odd.next = even.next
			odd = odd.next
		even.next = node
		return dummy
