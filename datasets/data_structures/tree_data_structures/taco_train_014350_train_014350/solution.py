def leftLeavesSum(h, side='r'):
	if h == None:
		return 0
	if h.left == h.right == None and side == 'l':
		return h.data
	return leftLeavesSum(h.left, 'l') + leftLeavesSum(h.right, 'r')
