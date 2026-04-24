for i in range(int(input())):
	input()
	a = list(map(int, input().split()))
	(lsum, rsum) = (0, sum(a))
	for e in a:
		rsum -= e
		if lsum == rsum:
			print('YES')
			break
		lsum += e
	else:
		print('NO')
