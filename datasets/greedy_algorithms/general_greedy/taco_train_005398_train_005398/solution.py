from heapq import heappush, heappop
from itertools import groupby
T = int(input())
for _ in range(T):
	(N, K) = list(map(int, input().split()))
	a = list(map(int, input().split()))
	h = []
	answer = 0
	for group in groupby(a):
		(value, it) = group
		m = sum((1 for elem in it))
		f = m * (m + 1) // 2
		answer += f
		for i in range(1, m // 2 + 1):
			k = (m - i) // (i + 1)
			r = (m - i) % (i + 1)
			new_f = r * (k + 1) * (k + 2) // 2 + (i + 1 - r) * k * (k + 1) // 2
			priority = new_f - f + 1
			heappush(h, priority)
			f = new_f
	for i in range(K):
		try:
			priority = heappop(h)
		except:
			break
		if priority == 0:
			break
		else:
			answer += priority
	print(answer)
