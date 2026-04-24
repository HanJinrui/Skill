from collections import deque

def solveQ(arr, queries, maxT):
	q1 = deque(sorted(arr, reverse=True))
	q2 = deque()
	for i in range(1, maxT + 1):
		if not q2 or q1[0] > q2[0]:
			e = q1.popleft()
		else:
			e = q2.popleft()
		if i in queries:
			print(e)
		e //= 2
		if e > 0:
			q2.append(e)
		if not q1:
			(q1, q2) = (q2, q1)
(n, m) = map(int, input().split())
multi = [int(x) for x in input().split()]
queries = [int(input()) for _ in range(m)]
maxQ = max(queries)
solveQ(multi, set(queries), maxQ)
