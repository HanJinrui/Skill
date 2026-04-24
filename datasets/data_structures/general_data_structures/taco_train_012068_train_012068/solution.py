from math import ceil
import heapq
t = int(input())
a = []
for _ in range(t):
	(r, X) = [int(i) for i in input().split()]
	A = [int(i) for i in input().split()]
	u = []
	heapq.heapify(u)
	energy = 0
	for i in range(ceil(r / 2) - 1, -1, -1):
		heapq.heappush(u, -A[i])
		if i != r - i - 1:
			heapq.heappush(u, -A[r - i - 1])
		energy += -heapq.heappop(u)
	if energy >= X:
		a.append('YES')
	else:
		a.append('NO')
for i in a:
	print(i)
