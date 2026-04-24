def subLinkedList(l1, l2):
	p = q = 0
	while l1:
		p = p * 10 + l1.data
		l1 = l1.next
	while l2:
		q = q * 10 + l2.data
		l2 = l2.next
	p = abs(p - q)
	r = str(p)
	for i in range(0, len(r)):
		print(r[i], end=' ')
