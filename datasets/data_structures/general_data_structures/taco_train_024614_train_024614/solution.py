def deleteK(head, k):
	if k == 1:
		return None
	t = head
	i = 0
	while t and t.next:
		i += 1
		if i == k - 1:
			t.next = t.next.next
			i = 0
		t = t.next
	return head
