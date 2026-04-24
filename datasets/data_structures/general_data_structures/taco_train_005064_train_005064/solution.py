def Push(x, stack1, stack2):
	stack1.append(x)

def Pop(stack1, stack2):
	if len(stack1) != 0:
		return stack1.pop(0)
	else:
		return -1
