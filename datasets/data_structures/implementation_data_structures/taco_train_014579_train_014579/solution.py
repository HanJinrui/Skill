for _ in range(int(input())):
	(n, k) = map(int, input().split())
	arr = input()
	(count, ans) = (0, 0)
	(I, M) = ([], [])
	for x in arr:
		if x == 'I':
			I.append(count)
			while M:
				tmp = M.pop(0)
				if abs(tmp - count) <= k:
					I.pop()
					ans += 1
					break
		elif x == 'M':
			M.append(count)
			while I:
				tmp = I.pop(0)
				if abs(tmp - count) <= k:
					M.pop()
					ans += 1
					break
		elif x == ':':
			count += 1
		elif x == 'X':
			I.clear()
			M.clear()
		count += 1
	print(ans)
