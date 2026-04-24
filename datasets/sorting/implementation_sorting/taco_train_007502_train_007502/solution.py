for e in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	res = []
	for i in range(n):
		for j in range(i + 1, n):
			if a[j] < a[i] or b[j] < b[i]:
				res.append((j + 1, i + 1))
				(b[i], b[j]) = (b[j], b[i])
				(a[j], a[i]) = (a[i], a[j])
	if not (a == sorted(a) and b == sorted(b)):
		print(-1)
		continue
	print(len(res))
	for i in res:
		print(*i)
