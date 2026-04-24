class Solution:

	def modifyTheList(self, head):
		l = []
		while head:
			l.append(head.data)
			head = head.next
		mid = len(l) // 2
		i = 0
		j = len(l) - 1
		while i < j:
			(l[i], l[j]) = (l[j], l[i])
			l[i] = l[i] - l[j]
			i += 1
			j -= 1
		for i in l:
			print(i, end=' ')
