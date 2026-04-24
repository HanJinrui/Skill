t = int(input())
for _ in range(t):
	n = int(input())
	data = [1] * (2 * n)
	data[::2] = (int(c) for c in input())
	data[1::2] = (int(c) for c in input())
	data.extend([1, 1])
	prev = 0
	count = 0
	for x in data:
		if prev and x and (count % 2 == 1):
			print('NO')
			break
		count += 1 - x
		prev = x
	else:
		print('YES')
