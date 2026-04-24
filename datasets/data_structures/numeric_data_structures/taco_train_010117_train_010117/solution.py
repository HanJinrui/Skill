n = int(input())
nl = list(map(int, input().split()))
p = list(set(range(1, n + 1)).difference(set(nl)))
j = 0
for i in range(n):
	if nl[i] == 0 and p[j] == i + 1:
		(p[j], p[j - 1]) = (p[j - 1], p[j])
		j += 1
	elif nl[i] == 0:
		j += 1
j = 0
for i in range(n):
	if nl[i] == 0:
		nl[i] = p[j]
		j += 1
print(*nl)
