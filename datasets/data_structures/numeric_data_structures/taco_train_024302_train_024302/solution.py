def minNumber(arr, N):
	s = sum(arr)
	d = s
	i = 1
	while i < s - 1:
		i = i + 1
		if s % i == 0:
			s = s + 1
			i = 1
	return s - d
