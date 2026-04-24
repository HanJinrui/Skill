(T, S) = input().split()
T = int(T)
S = int(S)
for _ in range(T):
	n = int(input())
	a = input().split()
	b = input().split()
	for i in range(n):
		a[i] = int(a[i])
		b[i] = int(b[i])
	a.sort()
	b.sort()
	if S == 1:
		if a[n - 1] >= b[n - 1] or a[0] >= b[0]:
			print('NO')
		else:
			flag = 0
			for i in range(1, n):
				if a[i - 1] != a[i] and a[i] not in b or a[i] >= b[i]:
					flag = 1
					break
			if flag == 1:
				print('NO')
			else:
				print('YES')
	elif n == 1:
		if a[0] >= b[0]:
			print('NO')
		else:
			print('YES')
	elif n == 2:
		di = {}
		for i in range(n):
			if a[i] not in di:
				di[a[i]] = 1
			else:
				di[a[i]] += 1
		for i in range(n):
			if b[i] not in di:
				di[b[i]] = 1
			else:
				di[b[i]] += 1
		flag = 0
		for i in di:
			if di[i] > n:
				flag = 1
		if flag == 1:
			print('NO')
		elif a[0] >= b[1] or (b[0] > a[1] and a[1] != a[0]):
			print('NO')
		else:
			print('YES')
	else:
		di = {}
		for i in range(n):
			if a[i] not in di:
				di[a[i]] = 1
			else:
				di[a[i]] += 1
		for i in range(n):
			if b[i] not in di:
				di[b[i]] = 1
			else:
				di[b[i]] += 1
		flag = 0
		for i in di:
			if di[i] > n:
				flag = 1
		if flag == 1:
			print('NO')
		else:
			flag1 = 0
			for i in range(n - 1):
				if a[i] != a[i + 1]:
					flag1 = 1
			if flag1 == 0 and a[0] > b[n - 1]:
				print('NO')
			else:
				flag2 = 0
				for i in range(n - 1):
					if b[i] != b[i + 1]:
						flag2 = 1
				if flag2 == 0 and a[0] > b[n - 1] and (flag1 == 1):
					print('NO')
				else:
					print('YES')
