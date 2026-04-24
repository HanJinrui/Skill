def isLengthEvenOrOdd(head):
	t = head
	i = 0
	while t:
		i += 1
		t = t.next
	return i % 2
