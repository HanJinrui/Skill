def sortedMerge(head1, head2):
	l = []
	l1 = []
	l2 = []
	t = head1
	while t:
		l.append(t.data)
		t = t.next
	t = head2
	while t:
		l1.append(t.data)
		t = t.next
	l2 = l1 + l
	l2.sort()
	for i in l2:
		print(i, end=' ')
