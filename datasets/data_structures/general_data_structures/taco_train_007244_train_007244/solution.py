def Country_at_war(arr, brr, n):
	count = 0
	for i in range(n):
		count += arr[i] > brr[i]
		count -= brr[i] > arr[i]
	return 'A' if count > 0 else 'B' if count < 0 else 'DRAW'
