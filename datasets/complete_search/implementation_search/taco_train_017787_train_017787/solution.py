n = int(input())
l = list(map(int, input().split()))
m = 0
for i in range(n):
	c = 0
	for j in range(i, n):
		c ^= l[j]
		m = max(m, c)
print(m)
