d = list(range(1000001))
for i in range(1000000):
	d[i + 1] = min(d[i + 1], d[i] + 1)
	j = 2
	while j <= i and j * i <= 1000000:
		d[i * j] = min(d[i] + 1, d[i * j])
		j += 1
for _ in range(int(input())):
	print(d[int(input())])
