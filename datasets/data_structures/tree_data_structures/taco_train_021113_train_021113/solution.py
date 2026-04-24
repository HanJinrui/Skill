def printPostOrder(inn, pre, n):
	if inn:
		ind = inn.index(pre.pop(0))
		temp = inn[ind]
		printPostOrder(inn[0:ind], pre, n)
		printPostOrder(inn[ind + 1:], pre, n)
		print(temp, end=' ')
		return
