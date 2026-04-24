n = int(input())
l = [*map(int, input().split())]
mx = 0
mxs = 0
m = 0
for i in range(n):
	s = 0
	for j in range(i, n):
		s = s + l[j]
		if s > (j - i + 1) * 100:
			m = max(m, j - i + 1)
print(m)
