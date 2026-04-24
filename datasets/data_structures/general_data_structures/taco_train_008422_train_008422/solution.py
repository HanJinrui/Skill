def intersetPoint(head1, head2):
	hs = set()
	n1 = head1
	n2 = head2
	while n1 != None:
		hs.add(n1)
		n1 = n1.next
	while n2 != None:
		if n2 in hs:
			return n2.data
		n2 = n2.next
	return -1
