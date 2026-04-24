def lastRoom(a, vp, n, m, k):
	current_room = 1
	for v in vp:
		if current_room == v[0]:
			current_room = v[1]
			if current_room in a and current_room != 1:
				break
		elif current_room == v[1]:
			current_room = v[0]
			if current_room in a and current_room != 1:
				break
	return current_room
