class Solution:

	def skipMdeleteN(self, head, M, N):
		while head != None:
			temp = head
			i = M
			while i != 0 and head != None:
				temp = head
				head = head.next
				i = i - 1
			i = N
			while i != 0 and head != None:
				head = head.next
				i = i - 1
