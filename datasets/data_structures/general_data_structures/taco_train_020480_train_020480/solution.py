def flatten(root):
	l = []
	h = root
	while h:
		l.append(h.data)
		h1 = h.bottom
		while h1:
			l.append(h1.data)
			h1 = h1.bottom
		h = h.next
	l.sort()
	a = b = Node(-1)
	for i in l:
		a.bottom = Node(i)
		a = a.bottom
	return b.bottom
