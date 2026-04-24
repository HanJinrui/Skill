for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	sm = 0
	ans = n
	a.sort()
	for i in range(len(a)):
		if sm + (a[i] + 1) // 2 > k:
			ans = i
			break
		sm += a[i]
	print(ans)
