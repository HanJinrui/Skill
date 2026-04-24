for _ in range(int(input())):
	list1 = list(map(int, input().split()))
	(N, x) = (list1[0], list1[1])
	A = list(map(int, input().split()))
	flag = True
	for i in range(1, N):
		if A[i] != A[i - 1]:
			flag = False
			break
	if flag:
		print(N * (N + 1) // 2)
		continue
	else:
		count = 0
		for i in range(N):
			product = A[i] / x
			if product == 1:
				count += 1
			for j in range(i + 1, N):
				product = product * A[j] / x
				if product == 1:
					count += 1
		print(count)
