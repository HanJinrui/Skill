for _ in range(int(input())):
	(n, k) = map(int, input().split())
	b = input()
	bo = 0
	for i in b:
		bo += 1 & int(i)
	bz = n - bo
	bs = n // k
	s = '0' * (bz // bs) + '1' * (bo // bs)
	f = (s + s[::-1]) * (bs // 2 + 1)
	if bz // bs + bo // bs == k:
		print(f[:n])
	else:
		print('IMPOSSIBLE')
