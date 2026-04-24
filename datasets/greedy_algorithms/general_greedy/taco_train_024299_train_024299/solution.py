for _ in range(int(input())):
	(n, k) = map(int, input().split())
	s = input()
	c = 0
	for i in s:
		x = (10 - int(i)) % 10
		t = k - x
		if t < 0:
			break
		k = t // 10 * 10 + x
		c += 1
	print(c)
