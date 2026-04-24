def isCircular(head):
	p = head
	while p != None:
		p = p.next
		if p == head:
			return 1
	return 0
