def quickSort(head):
	x = []
	while head:
		x.append(head.data)
		head = head.next
	x.sort()
	for i in x:
		print(i, end=' ')
