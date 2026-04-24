def pendulumArrangement(arr, n):
	arr.sort()
	arr1 = arr[0::2]
	arr2 = arr[1::2]
	return arr1[::-1] + arr2
