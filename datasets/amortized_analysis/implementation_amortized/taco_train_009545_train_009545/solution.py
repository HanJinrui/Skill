(n, m, k) = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
i = 0
while i < m:
	j = i + 1
	while j < m and (l[j] - 1 - i) // k == (l[i] - 1 - i) // k:
		j += 1
	i = j
	cnt += 1
print(cnt)
