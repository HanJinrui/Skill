T = int(input())
for t in range(0, T):
	N = int(input())
	n3 = -N % 3
	n5 = (N - n3 * 5) // 3
	if n5 < 0:
		print('-1')
	else:
		print(''.join(['555'] * n5 + ['33333'] * n3))
