n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
res = 0
for i in range(n):
	if a[i] != b[i]:
		res += 1
print('YES' if res <= 2 else 'NO')
