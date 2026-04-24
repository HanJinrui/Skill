def sumOfLastN_Nodes(head, n):
	l = []
	while head:
		l.append(head.data)
		head = head.next
	m = sum(l[-n:])
	return m
