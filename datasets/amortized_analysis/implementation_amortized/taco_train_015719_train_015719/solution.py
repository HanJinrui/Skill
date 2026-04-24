(n, m, k) = map(int, input().split())
lis = list(map(int, input().split()))
x = 0
i = 0
while i < m:
	y = i
	cur = (lis[i] - 1 - y) // k
	while i < m and (lis[i] - 1 - y) // k == cur:
		i += 1
	x += 1
print(x)
