for _ in range(int(input())):
	r = input()
	h = len(r)
	count = 0
	for i in range(2, h - 1, 2):
		if r[:i // 2] == r[i // 2:i] and r[i:i + (h - i) // 2] == r[i + (h - i) // 2:h]:
			count += 1
	print(count)
