def constructTree(postfix):
	chars = list(postfix)
	for i in chars:
		if i.isalpha():
			print(i, end=' ')
			last = chars.pop()
			if not last.isalpha():
				print(last, end=' ')
