def encode(arr):
	s = arr[0]
	n = 1
	for c in arr[1:]:
		if c == s[-1]:
			n += 1
		elif c != s[-1]:
			s += str(n) + c
			n = 1
	s += str(n)
	return s
