def getNth(head, k):
	for _ in range(k - 1):
		head = head.next
	return head.data
