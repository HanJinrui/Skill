for t in range(int(input())):
	n = int(input())
	c = [0] * 3
	while n != 0:
		c[n % 3] += 1
		n //= 3
	print(int(2 ** (c[1] - 1) * (3 ** (c[2] + 1) - 1)) % (10 ** 9 + 7))
