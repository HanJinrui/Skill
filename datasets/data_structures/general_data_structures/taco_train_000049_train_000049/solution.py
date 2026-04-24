def _push(a, n):
	return a

def _getMinAtPop(stack):
	while len(stack) != 0:
		print(min(stack), end=' ')
		a = stack.pop()
