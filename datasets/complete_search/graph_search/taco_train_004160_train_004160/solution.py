n = int(input())
s = list(map(int, input().split()))
for i in range(n):
	a = [1] * n
	while a[i]:
		a[i] = 0
		i = s[i] - 1
	print(i + 1, end=' ')
