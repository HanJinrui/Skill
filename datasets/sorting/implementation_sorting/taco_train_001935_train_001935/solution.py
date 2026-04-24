p = {}
for j in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	s = sum(a)
	for i in range(n):
		if s - a[i] in p:
			print('YES')
			print(j + 1, i + 1)
			print(*p[s - a[i]])
			exit()
	for x in range(n):
		p[s - a[x]] = [j + 1, x + 1]
print('NO')
