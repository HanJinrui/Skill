def compute(head):
	t = head
	s = ''
	while t:
		s += t.data
		t = t.next
	return s == s[::-1]
