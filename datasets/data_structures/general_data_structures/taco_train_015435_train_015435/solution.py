class Solution:

	def reverseBetween(self, head, m, n):
		K = []
		while head:
			K.append(head.data)
			head = head.next
		K[m - 1:n] = K[m - 1:n][::-1]
		L1 = LinkedList()
		for i in K:
			L1.append(i)
		return L1.head
