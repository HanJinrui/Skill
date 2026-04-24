def countTriplets(head, x):
	h1 = head
	count = 0
	while h1:
		m = {}
		h2 = h1.nxt
		while h2:
			value = x - (h1.val + h2.val)
			if value in m:
				count += 1
			else:
				m[h2.val] = 1
			h2 = h2.nxt
		h1 = h1.nxt
	return count
