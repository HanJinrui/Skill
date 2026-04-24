import math

def fractionalNodes(head, k):
	x = math.ceil(n / k)
	while x > 1:
		head = head.next
		x -= 1
	return head
