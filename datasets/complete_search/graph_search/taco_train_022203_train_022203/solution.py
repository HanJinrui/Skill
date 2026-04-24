(n, m, k) = map(int, input().split())
ban = list(map(int, input().split()))
if k == n or m > n * (n - 1) // 2 - k + 1:
	print('-1')
else:
	edges = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
	for i in range(1, k):
		a = min(ban[i], ban[0])
		b = max(ban[i], ban[0])
		edges.remove((a, b))
	special = None
	for i in range(n):
		if i + 1 not in ban:
			special = i
			break
	for i in range(n):
		if special == i:
			continue
		a = min(special, i) + 1
		b = max(special, i) + 1
		print(a, b)
		m -= 1
		edges.remove((a, b))
	for x in edges[:m]:
		print(x[0], x[1])
