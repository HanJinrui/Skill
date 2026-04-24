T = int(input())
for _ in range(T):
	x = int(input())
	p = x // 2
	if x % 2 == 1:
		print(p, p + 1)
	else:
		print(p + 1, p - 1)
