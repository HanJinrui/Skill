rd = lambda : list(map(int, input().split()))
rd()
a = sorted(rd(), reverse=True)
b = sorted(rd(), reverse=True)
if len(a) > len(b):
	print('YES')
	exit()
for i in range(len(a)):
	if a[i] > b[i]:
		print('YES')
		exit()
print('NO')
