def answer(arr, n):
	dif = arr[0] - arr[1]
	if dif == 0 or n % 2 == 0:
		return 'No'
	if arr[n // 2] != 1:
		return 'No'
	for i in range(1, n - 1):
		if abs(arr[i] - arr[i + 1]) != dif:
			return 'No'
	return 'Yes'
