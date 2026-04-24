def insertInMid(head, node):
	d = head
	n = head
	while n.next and n.next.next:
		d = d.next
		n = n.next.next
	node.next = d.next
	d.next = node
	return head
