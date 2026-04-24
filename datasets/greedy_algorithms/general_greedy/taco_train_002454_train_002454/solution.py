(N, K) = map(int, input().split())
A = list(map(int, input().split()))
swaps = 0
for i in range(N):
	if A[i] != N - i:
		j = A.index(N - i)
		(A[i], A[j]) = (A[j], A[i])
		swaps += 1
	if swaps >= K:
		break
print(' '.join(map(str, A)))
