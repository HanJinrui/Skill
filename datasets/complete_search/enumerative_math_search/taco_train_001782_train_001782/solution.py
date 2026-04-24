for _ in range(int(input())):
	N = int(input().split()[0])
	A = [int(s) for s in input().split()]
	for _ in range(N):
		print(sum((a * (b == '1') for (a, b) in zip(A, input()))))
