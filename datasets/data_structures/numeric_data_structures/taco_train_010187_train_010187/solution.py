def modularNode(head, k):
	l = -1
	i = 1
	while head:
		if i % k == 0:
			l = head.data
		i += 1
		head = head.next
	return l
