for _ in range(int(input())):
	(n, x) = map(int, input().split())
	d = dict.fromkeys(list(range(1, n + 1)))
	if n == 2:
		if x == 3:
			print('1 1 2')
		else:
			print(-1)
	else:
		for i in range(20):
			ni = 1 << i
			d[ni] = True
			if ni & n:
				msbn = i
			if ni & x:
				msbx = i
		if msbx > msbn:
			print(-1)
		elif not d[n] or x & n:
			val = 0
			for i in range(1, n + 1):
				if not d[i]:
					if i > 3:
						print('1 {} {}'.format(i, val))
					val |= i
			for i in d.keys():
				if i > n or not d[i]:
					continue
				if x & i:
					print('1 {} {}'.format(i, val))
					val |= i
				else:
					print('2 {} {}'.format(i, val))
					val ^= i
		else:
			print(-1)
