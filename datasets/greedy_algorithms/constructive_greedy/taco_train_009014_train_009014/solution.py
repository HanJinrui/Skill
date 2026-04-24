for _ in range(int(input())):
	(n, k) = map(int, input().split())
	w = list(map(int, input().split()))
	c = 1
	t = 0
	for i in w:
		if i > k:
			c = -1
			break
		elif i <= k:
			t += i
			if t > k:
				c += 1
				t = i
	print(c)
