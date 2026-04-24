t = int(input())
for i in range(t):
	flag = 0
	(o1, o2) = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	a = a + a[:o2 - 1]
	b = [0] * o2
	ones = 0
	ones = sum(a[:o2])
	if ones > o2 / 2:
		b[0] = 1
	for j in range(o2, len(a)):
		ones = ones + a[j] - a[j - o2]
		if ones > o2 / 2:
			b[(j + 1) % o2] += 1
	if any((i > o1 / 2 for i in b)):
		print(1)
	else:
		print(0)
