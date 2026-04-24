for _ in range(int(input())):
	(n, x) = map(int, input().split())
	arr = list(map(int, input().split()))
	rem = 0
	for i in range(n - 1):
		a = arr[i]
		d = a & rem
		(a, rem) = (a ^ d, rem ^ d)
		b = bin(a).count('1')
		if b <= x:
			x -= b
			rem ^= a
			a = 0
		elif x > 0:
			d = 0
			for j in range(31, -1, -1):
				if a & 1 << j != 0:
					d ^= 1 << j
					x -= 1
					if x == 0:
						break
			(a, rem) = (a ^ d, rem ^ d)
		arr[i] = a
	arr[-1] ^= rem
	if x == 1 or (n == 2 and x % 2 == 1):
		arr[-2] = 1
		arr[-1] ^= 1
	print(*arr)
