from collections import Counter
test = int(input())
for _ in range(test):
	n = int(input())
	A = list(map(int, input().split()))
	c = Counter(A)
	m = max(c.values())
	if m > n // 2 or len(c) <= 2:
		print('NO')
	else:
		print('YES')
		A.sort()
		print(*A)
		p = n // 2
		print(*A[p:] + A[:p])
