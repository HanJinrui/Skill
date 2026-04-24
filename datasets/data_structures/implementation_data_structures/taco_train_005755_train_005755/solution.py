n = int(input())
(a, b) = ({}, {})
ans = 1
t = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
	x = t[i]
	a[x] = a.get(x, 0) + 1
	b[a[x]] = b.get(a[x], 0) + 1
	if a[x] * b[a[x]] == i and i != n:
		ans = i + 1
	elif a[x] * b[a[x]] == i - 1:
		ans = i
print(ans)
