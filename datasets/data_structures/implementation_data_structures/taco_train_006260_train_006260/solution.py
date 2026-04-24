Max = 100001
(n, m) = map(int, input().split())
arr = map(int, input().split())
a = [0] * Max
b = [0] * Max
ans = ''
for i in arr:
	a[i] += 1
	b[a[i]] += 1
	ans += str([0, 1][1 if b[a[i]] == n else 0])
print(ans)
