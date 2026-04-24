def mergeList(h1, h2):
	(s, l) = (h1, h2)
	while h1 != None and h2 != None:
		k = h1.next
		l = h2.next
		h1.next = h2
		h2.next = k
		(h1, h2) = (k, l)
	return [s, l]
