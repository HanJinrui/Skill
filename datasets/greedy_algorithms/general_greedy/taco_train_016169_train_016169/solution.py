for i in range(int(input())):
	(N, X) = map(int, input().split())
	times = []
	friends = [1] * N
	for j in range(N):
		times.append(list(map(int, input().split())))
	times.sort(key=lambda x: x[1])
	ans = 0
	for i in range(1, N):
		for j in range(i):
			if times[i][0] <= times[j][1]:
				friends[j] += 1
		flag = False
		for l in range(i):
			if X == friends[l]:
				flag = True
				ans += 1
				break
		if flag:
			for k in range(i + 1):
				friends[k] -= 1
	print(ans)
