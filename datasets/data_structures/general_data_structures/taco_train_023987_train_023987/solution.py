from heapq import *
n = int(input())
o = [tuple(map(int, input().split())) for _ in range(n)]
o.sort(reverse=True)
x = 0
w = 0
h = []
while o or h:
	if h:
		(a, b) = heappop(h)
		x += a
		w += x - b
	else:
		x = o[-1][0]
	while o and o[-1][0] <= x:
		heappush(h, o.pop()[::-1])
print(w // n)
