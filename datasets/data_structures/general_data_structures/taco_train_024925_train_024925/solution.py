from collections import deque
(n, q) = map(int, input().strip().split())
arr = [int(s) for s in input().strip().split()]
for _ in range(q):
	d = int(input())
	window = deque(arr[:d])
	mm = m = max(window)
	for x in arr[d:]:
		window.append(x)
		if window.popleft() == m:
			m = max(window)
			mm = min(mm, m)
	print(mm)
