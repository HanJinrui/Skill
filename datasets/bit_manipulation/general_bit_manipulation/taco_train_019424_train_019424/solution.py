for t in range(int(input())):
	k = 0
	n = int(input())
	d = 2 ** 63
	while n > 1:
		while d >= n:
			d //= 2
		n -= d
		k += 1
	print(['Richard', 'Louise'][k % 2])
