def addNode(head, p, data):
	t = head
	c = 0
	while c != p:
		t = t.next
		c = c + 1
	x = Node(data)
	x.next = t.next
	x.prev = t
	t.next = x
