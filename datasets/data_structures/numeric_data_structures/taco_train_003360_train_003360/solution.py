for i in range(int(input())):
	x = int(input())
	if x < 1500:
		print(2 * x)
	else:
		print(x + 500 + 0.98 * x)
