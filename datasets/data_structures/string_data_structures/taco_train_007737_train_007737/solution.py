n = int(input())
v = list(map(int, input().split()))
ans = 'NO'
p = []
for i in range(n + 1):
	p.append(-1)
for i in range(n):
	p[v[i]] = i
for i in range(n - 1):
	for j in range(i + 1, min(n, i + 6)):
		if v[i] * 2 - v[j] >= 1 and v[i] * 2 - v[j] <= n and (p[v[i] * 2 - v[j]] < i):
			ans = 'YES'
			break
		if v[j] * 2 - v[i] >= 1 and v[j] * 2 - v[i] <= n and (p[v[j] * 2 - v[i]] > j):
			ans = 'YES'
			break
	if ans == 'YES':
		break
print(ans)
