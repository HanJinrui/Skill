import heapq
n = int(input())
maxh = []
minh = []
l = 0
while n != 0:
	q = list(map(int, input().split()))
	if q[0] == 1:
		x = heapq.heappushpop(minh, q[1])
		heapq.heappush(maxh, -x)
		l += 1
		if l % 3 == 0:
			x = heapq.heappop(maxh)
			heapq.heappush(minh, -x)
	elif len(minh) > 0:
		x = heapq.heappop(minh)
		print(x)
		heapq.heappush(minh, x)
	else:
		print('No reviews yet')
	n -= 1
