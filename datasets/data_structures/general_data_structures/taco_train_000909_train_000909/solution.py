def countNodesinLoop(head):
	x = {}
	i = 0
	while head:
		if head in x:
			return len(x) - x[head]
		x[head] = i
		i = i + 1
		head = head.next
	return 0
