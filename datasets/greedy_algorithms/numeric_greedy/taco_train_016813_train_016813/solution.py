(n, m) = map(int, input().split())
for j in range(m):
	s = set(map(int, input().split()[1:]))
	if all((-x not in s for x in s)):
		print('YES')
		exit()
print('NO')
