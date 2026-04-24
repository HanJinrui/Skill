from collections import Counter
(N, K) = (int(x) for x in input().split(' '))
A = (int(x) for x in input().split(' '))
C = Counter(A)
R = [1]
for (n, c) in C.items():
	R.append(0)
	for i in range(len(R) - 1, 0, -1):
		R[i] += R[i - 1] * c
		R[i] = R[i] % 1000000007
print(sum(R[:K + 1]) % 1000000007)
