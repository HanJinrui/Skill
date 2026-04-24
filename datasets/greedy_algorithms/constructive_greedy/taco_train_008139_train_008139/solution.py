from collections import Counter
n = int(input())
l = list(map(int, input().split()))
(m, x) = Counter(l).most_common(1)[0]
print(n - x)
ind = l.index(m)
for i in range(ind, -1, -1):
	if l[i] != m:
		print(1 if l[i] < m else 2, i + 1, i + 2)
for i in range(ind, n):
	if l[i] != m:
		print(1 if l[i] < m else 2, i + 1, i)
