def process(N, M, MAX):
	table[0][0] = [arr[0][0]]

	for i in range(1, M):
		table[0][i] = [table[0][i-1][0] + arr[0][i]]

	for i in range(1, N):
		table[i][0] = [table[i-1][0][0] + arr[i][0]]

	for i in range(1, N):
		for j in range(1, M):
			ans = set()
			val = arr[i][j]

			for v in table[i][j-1]:
				tmp = val + v
				if tmp <= MAX:
					ans.add(tmp)
			for v in table[i-1][j]:
				tmp = val + v
				if tmp <= MAX:
					ans.add(tmp)

			for v in table[i-1][j-1]:
				tmp = val + v
				if tmp <= MAX:
					ans.add(tmp)
			table[i][j] = sorted(ans)

	ans = table[N-1][M-1]
	if ans:
		if max(ans) > MAX:
			print(-1)
		else:
			print(max(ans))
	else:
		print(-1)


T = eval(input())
for i in range(T):
	N, M, MAX = list(map(int, input().split(" ")))
	arr = []
	for V in range(N):
		arr.append(list(map(int, input().split(" "))))
	table = [[[] for c in range(M)] for r in range(N)]
	process(N, M, MAX)
