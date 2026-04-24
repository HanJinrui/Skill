def stockBuySell(a, n):
	buy = 0
	sell = 0
	i = 1
	notPresent = True
	while i < n:
		buy = i - 1
		while i < n and a[i] > a[i - 1]:
			i += 1
		sell = i - 1
		if buy != sell:
			notPresent = False
			print('({} {})'.format(buy, sell), end=' ')
		i += 1
	if notPresent:
		print('No Profit', end=' ')
	print()
