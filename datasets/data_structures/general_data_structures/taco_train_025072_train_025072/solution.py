def deleteNode(head, key):
	p = c = head
	while c.data != key:
		p = c
		c = c.next
	p.next = c.next

def reverse(head):
	p = None
	c = head
	while c:
		cnext = c.next
		c.next = p
		p = c
		c = cnext
	c = head
	while c.next != head:
		(c.data, c.next.data) = (c.next.data, c.data)
		c = c.next
