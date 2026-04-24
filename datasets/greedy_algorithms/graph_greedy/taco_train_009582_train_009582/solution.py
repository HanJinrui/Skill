def find(a):
	global k, tot
	if a > n * (n - 1):
		return 1
	while a > tot + (n - k) * 2:
		tot += (n - k) * 2
		k += 1
	if a & 1:
		return k
	return (a - tot) // 2 + k
for _ in range(int(input())):
	(n, l, r) = map(int, input().split())
	global k, tot
	k = 1
	tot = 0
	li = []
	for i in range(l, r + 1):
		li.append(find(i))
	print(*li)
