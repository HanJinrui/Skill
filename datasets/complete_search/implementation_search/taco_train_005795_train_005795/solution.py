t = int(input())
for i in range(t):
	p = list(map(int, input().split()))
	if sum(p) < 4:
		print('NO')
	else:
		print('YES')
