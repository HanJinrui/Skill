def game(arr, brr, n):
	energy = 0
	for i in range(n):
		energy += arr[i] - brr[i]
		if energy < 0:
			return 'Game Over'
		energy += i + 1
	return 'You Win! ' + str(energy)
