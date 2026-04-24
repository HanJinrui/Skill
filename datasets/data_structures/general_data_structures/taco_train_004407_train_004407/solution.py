def alternatingSplitList(head):
	global a, b
	temp = head
	bool = 1
	while temp:
		if bool:
			a = append(a, temp.data)
			bool = 0
		else:
			bool = 1
			b = append(b, temp.data)
		temp = temp.next
