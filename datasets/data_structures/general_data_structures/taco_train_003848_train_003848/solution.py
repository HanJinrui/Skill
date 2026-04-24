def decimalValue(head):
	s = ''
	tmp = head
	while tmp:
		s += str(tmp.data)
		tmp = tmp.next
	return int(s, 2) % 1000000007
