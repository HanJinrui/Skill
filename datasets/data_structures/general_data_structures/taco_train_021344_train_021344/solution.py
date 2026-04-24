def countOfElements(a, n, x):
	return len(list(filter(lambda i: i <= x, a)))
