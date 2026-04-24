(r, c) = map(int, input().split())
m1 = []
m2 = []
for i in range(r):
	s = list(map(int, input().split()))
	m1.append(min(s))
	m2.append(s)
n = []
for j in range(c):
	x = []
	for k in range(r):
		x.append(m2[k][j])
	n.append(max(x))
f = 0
for z in m1:
	if z in n:
		print(z)
		f = 1
		break
if f == 0:
	print('GUESS')
