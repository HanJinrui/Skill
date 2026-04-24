def SumArray(arr, n):
	s = sum(map(int, arr))
	for x in range(n):
		arr[x] = s - int(arr[x])
