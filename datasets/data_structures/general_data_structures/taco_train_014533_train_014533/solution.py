class Solution:

	def getCount(self, head):
		N = 1
		while head.next != None:
			head = head.next
			N += 1
		return N
