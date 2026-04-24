def lucky(arr, n):
	return len(set([sum(map(int, [*str(item)])) for item in arr]))
