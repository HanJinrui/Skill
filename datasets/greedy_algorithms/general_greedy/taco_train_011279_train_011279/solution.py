import heapq
(n, k) = map(int, input().split())
a = []
for v in input().split():
	heapq.heappush(a, int(v))
for i in range(k):
	heapq.heappush(a, -heapq.heappop(a))
print(sum(a))
