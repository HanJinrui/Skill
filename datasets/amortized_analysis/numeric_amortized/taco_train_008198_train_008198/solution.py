for _ in range(int(input())):
	n = int(input())
	p = list(map(int, input().split()))
	pinv = [0] * n
	for i in range(n):
		pinv[p[i]] = i
	(idxmin, idxmax) = (pinv[0], pinv[0])
	ans = 1
	for w in range(2, n + 1):
		if w % 2 == 1:
			(idxmin, idxmax) = (min(idxmin, pinv[w // 2]), max(idxmax, pinv[w // 2]))
		ans += max(0, min(idxmin, n - w) - max(idxmax + 1 - w, 0) + 1)
	print(ans)
