def rev(q):
	st = []
	while q.qsize():
		st.append(q.get())
	while st:
		q.put(st.pop())
	return q
