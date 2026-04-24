def PalinArray(arr, n):
	return all((str(num) == str(num)[::-1] for num in arr))
