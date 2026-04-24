def sortedInsert(head, x):
	new = Node(x)
	if x < head.data:
		new.next = head
		head.prev = new
		return new
	curr = head
	while curr and curr.next and (curr.next.data < x):
		curr = curr.next
	new.next = curr.next
	new.prev = curr
	if curr.next:
		curr.next.prev = new
	curr.next = new
	return head
