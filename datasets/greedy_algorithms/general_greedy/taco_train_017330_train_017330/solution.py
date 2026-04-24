(n, k) = map(int, input().split())
arr = []
for i in range(n):
	(l, r) = map(int, input().split())
	arr.append([r, l, i])
arr.sort()
ans = []
for i in range(201):
	s = 0
	a = []
	for j in arr:
		if i <= j[0] and i >= j[1]:
			s += 1
			if s > k:
				ans.append(j[2] + 1)
				a.append(j)
	for j in a:
		arr.remove(j)
print(len(ans))
print(*sorted(ans))
