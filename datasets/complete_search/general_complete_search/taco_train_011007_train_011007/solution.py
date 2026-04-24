import sys
(n, k) = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
ans = 0
i = 0
while i < n:
	ii = i
	while ii < n - 1 and x[ii + 1] - x[i] <= k:
		ii += 1
	ans += 1
	while i < n and x[i] - x[ii] <= k:
		i += 1
print(ans)
