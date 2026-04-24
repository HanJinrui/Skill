def swapkthnode(head, num, k):
	if k > n:
		return head
	c = head
	p = None
	b = head
	d = None
	for i in range(1, k):
		p = c
		c = c.next
	for i in range(1, n - k + 1):
		d = b
		b = b.next
	if p != None:
		p.next = b
	if d != None:
		d.next = c
	(c.next, b.next) = (b.next, c.next)
	if k == 1:
		head = b
	if k == n:
		head = c
	return head
