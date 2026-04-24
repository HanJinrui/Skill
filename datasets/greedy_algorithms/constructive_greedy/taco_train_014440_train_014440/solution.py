import sys
input = lambda : sys.stdin.readline().rstrip()
I = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
T = int(input())
for _ in range(T):
	(R, C, K) = map(int, input().split())
	X = [[1 if a == 'R' else 0 for a in input()] for _ in range(R)]
	s = sum([sum(x) for x in X])
	a = s // K
	r = s - K * a
	Y = [a] * (K - r) + [a + 1] * r
	Y[-1] += 1
	k = 0
	ANS = [[''] * C for _ in range(R)]
	for i in range(R):
		for j in range(C)[::-1 if i % 2 else 1]:
			ANS[i][j] = I[k]
			if X[i][j] and Y[k]:
				Y[k] -= 1
				if Y[k] == 0:
					k += 1
	for a in ANS:
		print(''.join(a))
