for _ in range(int(input())):
	T = int(input())
	N = [int(i) for i in input().split()]
	A = 1
	for i in range(T // 2 + 1):
		if N[i] == A:
			A = A + 1
	print('no' if N != N[::-1] or A < 8 else 'yes')
