(n, k) = map(int, input().split())
a = [int(_) for _ in input().split()]
mp = {}
res = 0
pos = 0
t = 0
for i in range(0, n):
	if a[i] in mp:
		mp[a[i]] += 1
	else:
		mp[a[i]] = 1
	while pos <= i and k <= mp[a[i]]:
		mp[a[pos]] -= 1
		res += n - i
		pos += 1
print(res)
