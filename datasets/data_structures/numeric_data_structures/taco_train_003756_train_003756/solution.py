t = int(input())
for _ in range(t):
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	ugly = [0] * k
	prev = -1
	same = 0
	for i in range(n - 1):
		if prev != -1 and prev != a[i + 1] and (a[i + 1] != a[i]) and (prev != a[i]):
			ugly[a[i] - 1] -= 1
		if a[i] != a[i + 1]:
			ugly[a[i] - 1] += 1
			ugly[a[i + 1] - 1] += 1
			prev = a[i]
		elif a[i] == a[i + 1]:
			same += 1
	ugly = [n - i - 1 - same for i in ugly]
	print(*ugly)
