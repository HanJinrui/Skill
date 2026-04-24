class Solution:

	def insertionSort(self, head):
		x = []
		while head:
			x.append(head.data)
			head = head.next
		for i in sorted(x):
			print(i, end=' ')
