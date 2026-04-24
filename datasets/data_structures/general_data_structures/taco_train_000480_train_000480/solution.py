for inputs in range(int(input())):
	rpn = ''
	stack = []
	for i in input():
		if i.isalpha():
			rpn += i
		elif i == ')':
			rpn += stack.pop()
			stack.pop()
		else:
			stack.append(i)
	print(rpn)
