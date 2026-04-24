n = int(input())
v = input().split()
if v[-1] != '0':
	print('NO')
else:
	if n >= 2 and v[-2] == '0':
		for i in range(n - 3, -1, -1):
			if v[i] == '0':
				v[i] = '(' + v[i]
				v[i + 1] = '(' + v[i + 1]
				v[-2] = v[-2] + '))'
				break
		else:
			print('NO')
			exit()
	print('YES')
	print('->'.join(v))
