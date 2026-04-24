(n, k) = map(int, input().split())
A = list(map(int, input().split()))
from itertools import accumulate
C = [0] + A
C = list(accumulate(C))
A = [0] + A
P = [0] * (n + 1)
x = 0
for i in range(1, n + 1):
	P[i] = x
	if A[i] > 1:
		x = i
INF = 2 * 10 ** 18 + 1
ans = 0
for i in range(1, n + 1):
	p = 1
	j = i
	while j:
		if p * A[j] < INF:
			s = C[i] - C[j - 1]
			p *= A[j]
			if p % k == 0:
				d = p // k - s
				if 0 <= d <= j - P[j] - 1:
					ans += 1
		else:
			break
		j = P[j]
print(ans)
