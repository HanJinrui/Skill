def getNthFromLast(head, n):
	x = head
	l = []
	while x:
		l.append(x.data)
		x = x.next
	if n <= len(l):
		return l[len(l) - n]
	return -1
