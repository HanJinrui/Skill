n = int(input())
h = []
for i in range(n):
	h.append(sorted(input().split()))
prev = ''
for i in (int(x) - 1 for x in input().split()):
	cur = h[i][0] if h[i][0] > prev else h[i][1]
	if cur < prev:
		print('NO')
		exit()
	prev = cur
print('YES')
