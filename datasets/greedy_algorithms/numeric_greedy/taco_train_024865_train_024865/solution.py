for _ in range(int(input())):
	N = int(input())
	for _ in range(N):
		input()
	K = 0
	while N >= 3:
		K += N
		N >>= 1
	print(K)
