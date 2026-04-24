read = lambda : map(int, input().split())
n = int(input())
ed = []
for i in range(n - 1):
	(u, v) = read()
	ed.append((u, v))
c = [0] + list(read())
cnt = [0] * (n + 1)
for (u, v) in ed:
	if c[u] != c[v]:
		cnt[u] += 1
		cnt[v] += 1
all = sum(cnt) // 2
for i in range(1, n + 1):
	if cnt[i] == all:
		print('YES')
		print(i)
		exit()
print('NO')
