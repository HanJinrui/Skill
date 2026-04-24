for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	(e, o) = ([], [])
	for i in range(n):
		if a[i] % 2 == 0:
			e.append(i + 1)
		else:
			o.append(i + 1)
	if o == []:
		print('NO')
	elif len(e) == 1 and n == 3:
		print('NO')
	else:
		print('YES')
		if len(o) >= 3:
			print(*o[:3])
		else:
			print(e[0], e[1], o[0])
