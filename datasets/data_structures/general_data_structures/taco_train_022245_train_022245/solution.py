import heapq as hq
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ans = [1] * n
	start = 0
	time = 1
	first = [(-a[start], start)]
	hq.heapify(first)
	while len(first):
		x = hq.heappop(first)
		ans[x[1]] = time
		time += 1
		start += 1
		if start < n:
			hq.heappush(first, (-a[start], start))
			start += 1
		if start < n:
			hq.heappush(first, (-a[start], start))
	print(*ans)
