(n, m) = map(int, input().split())
n //= m
A = list(map(int, input().split()))
S = [n] * m
L = []
for (i, a) in enumerate(A):
	a -= 1
	if m > a and S[a]:
		S[a] -= 1
	else:
		L.append(i)
for (i, s) in enumerate(S, 1):
	for _ in range(s):
		A[L.pop()] = i
print(n, sum(S))
print(*A)
