from collections import deque
t = int(input())
for _ in range(t):
	l = list(map(int, input().split()))
	(n, l) = (l[0], l[1:])
	min_ = l[1] + l[2]
	c2 = sum(l) - l[2] - l[5]
	c5 = sum(l) - l[1] - l[4]
	c6 = sum(l) - l[1]
	q = deque()
	q.append((2, c2))
	q.append((5, c5))
	q.append((6, c6))
	while q:
		(num, cost) = q.popleft()
		if cost >= min_:
			continue
		if n % num == 0:
			min_ = min(min_, cost)
		q.append((num * 10 + 2, cost + c2))
		q.append((num * 10 + 5, cost + c5))
		q.append((num * 10 + 6, cost + c6))
	print(min_)
