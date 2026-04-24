def convert(head):
	li = []
	temp = head
	while temp:
		li.append(temp.data)
		temp = temp.next
	li.reverse()
	print(*li)
