def decodeHuffmanData(root, str):
	ans = ''
	tmp = root
	for i in str:
		if i == '0':
			tmp = tmp.left
		elif i == '1':
			tmp = tmp.right
		if not tmp.left and (not tmp.right):
			ans += tmp.data
			tmp = root
	return ans
