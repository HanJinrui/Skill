def removeDuplicates(head):
	f = head
	while f.next:
		if f.next.data == f.data:
			f.next = f.next.next
		else:
			f = f.next
