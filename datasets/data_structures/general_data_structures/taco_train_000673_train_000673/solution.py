from heapq import *
n = int(input())
neighbors = {}
for x in range(n):
	neighbors[x] = []
for i in range(n - 1):
	(a, b) = map(int, input().split())
	neighbors[a - 1].append(b - 1)
	neighbors[b - 1].append(a - 1)

def search(source):
	ans = 0
	cur_max = 0
	cur_len = 0
	heap = [source]
	vis = [False for i in range(n)]
	while len(heap) > 0:
		x = heappop(heap)
		cur_max = max(cur_max, x)
		cur_len += 1
		vis[x] = True
		if cur_max - source + 1 == cur_len:
			ans += 1
		for y in neighbors[x]:
			if y >= source and vis[y] == False:
				heappush(heap, y)
	return ans
ans = 0
prev = 0
for x in range(n - 1, -1, -1):
	neigh = 0
	plus = 0
	for y in neighbors[x]:
		if y > x:
			neigh += 1
		if y == x + 1:
			plus = 1
	if plus == neigh and plus == 1:
		prev += 1
	else:
		prev = search(x)
	ans += prev
print(ans)
