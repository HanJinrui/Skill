def deleteElement(arr, n, k):
	s = []
	for i in arr:
		while s and k and (s[-1] < i):
			s.pop()
			k -= 1
		s.append(i)
	return s
