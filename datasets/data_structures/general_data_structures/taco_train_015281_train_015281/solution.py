def reverseDLL(head):
	(p, c) = (None, head)
	while c:
		c.prev = c.next
		c.next = p
		(p, c) = (c, c.prev)
	return p
