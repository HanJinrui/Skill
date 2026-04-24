import collections as c, sys
(N, M, P) = list(map(int, sys.stdin.readline().split()))
A = c.defaultdict(lambda : c.defaultdict(int))
for _ in range(P):
	(i, j) = list(map(int, sys.stdin.readline().split()))
	if j - 1 in A[i - 1]:
		A[i - 1][j - 1] += 1
	else:
		A[i - 1][j - 1] = j
for i in range(N):
	for (j, v) in A[i].items():
		if j == M - 1:
			continue
		x = A[i][j + 1] if j + 1 in A[i] else j + 1
		if A[i][j] > x:
			print(-1)
			break
	else:
		x = A[i][M - 1] if M - 1 in A[i] else M - 1
		print(x - A[i][0])
