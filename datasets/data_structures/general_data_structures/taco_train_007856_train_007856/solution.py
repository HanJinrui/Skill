def compare(head1, head2):
	a = ''
	b = ''
	t = head1
	r = head2
	while t:
		a += t.data
		t = t.next
	while r:
		b += r.data
		r = r.next
	if a == b:
		return 0
	elif a > b:
		return 1
	return -1
