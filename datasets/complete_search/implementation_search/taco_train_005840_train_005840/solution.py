n = int(input())
p = 0
for i in range(1, n):
	p = (p + i) % n
	print(p + 1, end=' ')
