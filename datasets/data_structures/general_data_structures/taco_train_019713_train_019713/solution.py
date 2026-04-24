def delNode(head, k):
	if k == 1:
		return head.next
	p = head
	for _ in range(k - 2):
		p = p.next
	p.next = p.next.next
	return head
