import heapq

def maximised_height(arr, n, m):
	heapq.heapify(arr)
	count = 1
	while arr and m >= count:
		item = heapq.heappop(arr)
		while arr and item < arr[0] and (m >= count):
			item += 1
			m -= count
		count += 1
	if not arr:
		count -= 1
	while m >= count:
		item += 1
		m -= count
	return item
