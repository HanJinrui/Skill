n = int(input())
l = list(map(int, input().split()))[::-1]
k = 0
p = -1
while k != n:
	l = l[::-1]
	p += 1
	for i in range(n):
		if l[i] != -1 and l[i] <= k:
			k += 1
			l[i] = -1
print(p)
