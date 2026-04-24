for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	ls = sorted(l)
	j = 0
	b = []
	for i in l:
		if i == ls[j]:
			j += 1
		else:
			b.append(i)
	if b == sorted(b):
		print('YES')
	else:
		print('NO')
