ans = []
(x, y) = map(int, input().split())
for _ in range(x):
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	L = list(zip(A, B))
	L.sort()
	co = 1
	for i in range(y - 1):
		if L[i][1] > L[i + 1][1]:
			co += 1
	ans.append([co, _])
ans.sort()
for i in ans:
	print(i[1] + 1)
