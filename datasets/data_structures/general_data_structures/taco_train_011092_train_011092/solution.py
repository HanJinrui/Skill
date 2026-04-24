def areIdentical(head1, head2):
	p = head1
	q = head2
	while p and q:
		if p.data == q.data:
			p = p.next
			q = q.next
		else:
			return 0
	return 1
