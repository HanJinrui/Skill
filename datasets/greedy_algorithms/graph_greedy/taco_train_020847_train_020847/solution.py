N = int(input())
P = [0, 0] + list(map(int, input().split()))
S = [0] + list(map(int, input().split()))
for i in range(2, N + 1):
	if S[i] != -1 and (S[P[i]] == -1 or S[P[i]] > S[i]):
		S[P[i]] = S[i]
a = S[:]
for i in range(2, N + 1):
	if S[i] != -1:
		a[i] = S[i] - S[P[i]]
		if a[i] < 0:
			print(-1)
			exit()
	else:
		a[i] = 0
print(sum(a))
