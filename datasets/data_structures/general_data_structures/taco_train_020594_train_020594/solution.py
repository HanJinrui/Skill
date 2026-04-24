def inPlace(root):
	h = root
	li = []
	while h:
		li.append(h.data)
		h = h.next
	h = root
	while h:
		h.data = li.pop(0)
		h = h.next
		if h != None:
			h.data = li.pop()
			h = h.next
	return root
