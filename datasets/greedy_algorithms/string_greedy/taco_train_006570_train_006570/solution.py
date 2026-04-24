T = int(input())
for t in range(T):
	n = int(input())
	x = n // 2
	print('a' * x + 'bc'[:n - x - max(0, x - 1)] + 'a' * max(0, x - 1))
