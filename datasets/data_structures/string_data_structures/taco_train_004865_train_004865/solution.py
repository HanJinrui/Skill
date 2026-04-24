class Solution:

	def isPalindrome(self, head):
		a = []
		while head:
			a.append(head.data)
			head = head.next
		return a == a[::-1]
