def swap(a, i):
	j = n - i - 1
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
q = int(input())
for i in range(q):
	n = int(input())
	a = [int(t) for t in input().split()]
	ans = []
	ans.append([0, 0, 0, 0])
	mid = n // 2
	flag = True
	if n == 2 and a[0] == a[1]:
		flag = False
	for k in range(1, mid + 1):
		tmp = []
		l = mid - k
		if n % 2 == 0:
			r = mid + k - 1
		else:
			r = mid + k
		if k == 1 and n % 2 == 0:
			if a[l] > a[r]:
				ans.append([0, -1, -1, 1])
			elif a[l] < a[r]:
				ans.append([-1, 1, 0, -1])
			else:
				flag = False
				break
			continue
		if n % 2 == 0:
			curr = -1
			if a[l] > a[l + 1] and a[r - 1] > a[r] and (ans[k - 1][2] >= 0):
				curr = ans[k - 1][2]
			if a[l] > a[r - 1] and a[l + 1] > a[r] and (ans[k - 1][3] >= 0):
				if ans[k - 1][3] < curr or curr == -1:
					curr = ans[k - 1][3]
			tmp.append(curr)
			curr = -1
			if a[r] > a[l + 1] and a[r - 1] > a[l] and (ans[k - 1][2] >= 0):
				curr = ans[k - 1][2] + 1
			if a[r] > a[r - 1] and a[l + 1] > a[l] and (ans[k - 1][3] >= 0):
				if ans[k - 1][3] + 1 < curr or curr == -1:
					curr = ans[k - 1][3] + 1
			tmp.append(curr)
			curr = -1
			if a[l] < a[l + 1] and a[r - 1] < a[r] and (ans[k - 1][0] >= 0):
				curr = ans[k - 1][0]
			if a[l] < a[r - 1] and a[l + 1] < a[r] and (ans[k - 1][1] >= 0):
				if ans[k - 1][1] < curr or curr == -1:
					curr = ans[k - 1][1]
			tmp.append(curr)
			curr = -1
			if a[r] < a[l + 1] and a[r - 1] < a[l] and (ans[k - 1][0] >= 0):
				curr = ans[k - 1][0] + 1
			if a[r] < a[r - 1] and a[l + 1] < a[l] and (ans[k - 1][1] >= 0):
				if ans[k - 1][1] + 1 < curr or curr == -1:
					curr = ans[k - 1][1] + 1
			tmp.append(curr)
		if n % 2 == 1:
			curr = -1
			if a[l] > a[l + 1] and a[r - 1] < a[r] and (ans[k - 1][2] >= 0):
				curr = ans[k - 1][2]
			if a[l] > a[r - 1] and a[l + 1] < a[r] and (ans[k - 1][3] >= 0):
				if ans[k - 1][3] < curr or curr == -1:
					curr = ans[k - 1][3]
			tmp.append(curr)
			curr = -1
			if a[r] > a[l + 1] and a[r - 1] < a[l] and (ans[k - 1][2] >= 0):
				curr = ans[k - 1][2] + 1
			if a[r] > a[r - 1] and a[l + 1] < a[l] and (ans[k - 1][3] >= 0):
				if ans[k - 1][3] + 1 < curr or curr == -1:
					curr = ans[k - 1][3] + 1
			tmp.append(curr)
			curr = -1
			if a[l] < a[l + 1] and a[r - 1] > a[r] and (ans[k - 1][0] >= 0):
				curr = ans[k - 1][0]
			if a[l] < a[r - 1] and a[l + 1] > a[r] and (ans[k - 1][1] >= 0):
				if ans[k - 1][1] < curr or curr == -1:
					curr = ans[k - 1][1]
			tmp.append(curr)
			curr = -1
			if a[r] < a[l + 1] and a[r - 1] > a[l] and (ans[k - 1][0] >= 0):
				curr = ans[k - 1][0] + 1
			if a[r] < a[r - 1] and a[l + 1] > a[l] and (ans[k - 1][1] >= 0):
				if ans[k - 1][1] + 1 < curr or curr == -1:
					curr = ans[k - 1][1] + 1
			tmp.append(curr)
		ans.append(tmp)
	if not flag or max(ans[mid]) == -1:
		print(-1)
	else:
		print(min([x for x in ans[mid] if x >= 0]))
