from heapq import *
(n, k) = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
ans = 0
while h[0] < k:
	if n < 2:
		ans = -1
		break
	n -= 1
	x = heappop(h)
	y = heappop(h)
	heappush(h, x + 2 * y)
	ans += 1
print(ans)
