for _ in range(int(input())):
	x = input()
	y = input()
	ans = 'Yes'
	for i in range(len(x)):
		if x[i] != y[i] and x[i] != '?' and (y[i] != '?'):
			ans = 'No'
			break
	print(ans)
