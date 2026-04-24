(n, L) = map(int, input().split())
k = list(map(int, input().split()))
s = list(map(int, input().split()))
for i in range(L):
	s = sorted(((si + 1) % L for si in s))
	if s == k:
		print('YES')
		exit()
print('NO')
