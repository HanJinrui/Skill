t = int(input())
for _ in range(t):
	n = int(input())
	l = []
	for i in range(n):
		l.append(input().split(' ', 2))
	res = 'Begin'
	for i in range(n - 1, -1, -1):
		res = res + ' ' + l[i][1] + ' ' + l[i][2]
		print(res)
		res = 'Right' if l[i][0] == 'Left' else 'Left'
