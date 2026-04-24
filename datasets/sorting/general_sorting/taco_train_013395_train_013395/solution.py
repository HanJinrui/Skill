n, s, e = [int(i) for i in input().split()]

res = 0
a = []
for i in range(n):
	x, p = [int(j) for j in input().split()]
	a.append([min(max(1, x-p, s), e), max(min(x+p, e), s)])

a.sort(key = lambda x:x[0])

tlen = e-s+1
clen = 0
i = 1
curr = a[0][1]
clen += (max(0, a[0][0]-s))
while i < n:
	if curr > a[i][0]:
		curr = max(curr, a[i][1])
		i += 1
	else:
		clen += (a[i][0] - curr)
		curr = a[i][1]
		i += 1
clen += (max(0, e - curr))
print(clen)
